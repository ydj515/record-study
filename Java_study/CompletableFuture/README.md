# CompletableFuture

- 2014년에 발표된 java 8에서 처음 도입
- 비동기 프로그래밍 지원
- Lambda, Method reference 등 Java 8의 새로운 기능 지원
- Future와 completionStage를 구현

Method reference란?

- `::` 연산자를 이용해서 함수에 대한 참조를 간결하게 표현
- method reference
- static method reference
- instance method reference
- constructor method reference

```java
@RequiredArgsConstructor
public static class Person {
    @Getter
    private final String name;
    public Boolean compareTo(Person o) {
        return o.name.compareTo(name) > 0;
    }
}

public static void print(String name) {
    System.out.println(name);
}
public static void main(String[] args) {
    var target = new Person("f");
    Consumer<String> staticPrint = MethodReferenceExample::print;
    Stream.of("a", "b", "g", "h")
        .map(Person::new) // constructor reference
        .filter(target::compareTo) // method reference
        .map(Person::getName) // instance method reference
        .forEach(staticPrint); // static method reference
}
```

### Future

- 비동기적인 작업을 수행
- 해당 작업이 완료되면 결과를 반환하는 인터페이스

```java
public interface Future<V> {
    boolean cancel(boolean mayInterruptIfRunning);
    boolean isCancelled();
    boolean isDone();
    V get() throws InterruptedException, ExecutionException;
    V get(long timeout, TimeUnit unit)
    throws InterruptedException, ExecutionException, TimeoutException;
}
```

이제 설명할 메소드를 이해하기 위해서 FutureHelpler를 작성하였다.

```java
// 새로운 쓰레드를 생성하여 1을 반환
public static Future<Integer> getFuture() {
    var executor = Executors.newSingleThreadExecutor();
    try {
        return executor.submit(() -> {
            return 1;
        });
    } finally {
        executor.shutdown();
    }
}

// 새로운 쓰레드를 생성하고 1초 대기 후 1을 반환
public static Future<Integer> getFutureCompleteAfter1s() {
    var executor = Executors.newSingleThreadExecutor();
    try {
        return executor.submit(() -> {
            Thread.sleep(1000);
        return 1;
        });
    } finally {
        executor.shutdown();
    }
}
```

#### isDone(), isCancelled()

- future의 상태를 반환
- isDone: task가 완료되었다면, 원인과 상관없이 true 반환
- isCancelled: task가 명시적으로 취소된 경우, true 반환

그림

#### get()

- 결과를 구할 때까지 thread가 계속 block
- future에서 무한 루프나 오랜 시간이 걸린다면 thread가 blocking 상태 유지

```java
Future future = FutureHelper.getFuture();
assert !future.isDone();
assert !future.isCancelled();

var result = future.get();
assert result.equals(1);
assert future.isDone(); // true
assert !future.isCancelled(); // false
```

#### get(long timeout, TimeUnit unit)

- 결과를 구할 때까지 timeout동안 thread가 block
- timeout이 넘어가도 응답이 반환되지 않으면 TimeoutException 발생

```java
Future future = FutureHelper.getFutureCompleteAfter1s();
var result = future.get(1500, TimeUnit.MILLISECONDS);
assert result.equals(1);
Future futureToTimeout = FutureHelper.getFutureCompleteAfter1s();
Exception exception = null;
try {
    futureToTimeout.get(500, TimeUnit.MILLISECONDS);
} catch (TimeoutException e) {
    exception = e;
}
assert exception != null;
```

#### cancel(booleanmayInterruptIfRunning)

- future의 작업 실행을 취소
- 취소할 수 없는 상황이라면 false를 반환
- mayInterruptIfRunning가 false라면 시작하지 않은 작업에 대해서만 취소

```java
Future future = FutureHelper.getFuture();
var successToCancel = future.cancel(true);
assert future.isCancelled();
assert future.isDone(); // true
assert successToCancel; // true
successToCancel = future.cancel(true); // false
assert future.isCancelled();
assert future.isDone();
assert !successToCancel;
```

Future 인터페이스의 한계

- cancel을 제외하고 외부에서 future를 컨트롤할 수 없다
- 반환된 결과를 get() 해서 접근하기 때문에 비동기 처리가 어렵다
- 완료되거나 에러가 발생했는지 구분하기 어렵다

```java
Future futureToCancel = FutureHelper.getFuture();
futureToCancel.cancel(true);
assert futureToCancel.isDone();
Future futureWithException = FutureHelper.getFutureWithException();
Exception exception = null;
try {
futureWithException.get();
} catch (ExecutionException e) {
exception = e;
}
assert futureWithException.isDone();
```

### CompletionStage

```java
public interface CompletionStage<T> {
    public <U> CompletionStage<U> thenApply(Function<? super T,? extends U> fn);
    public <U> CompletionStage<U> thenApplyAsync(Function<? super T,? extends U> fn);
    public CompletionStage<Void> thenAccept(Consumer<? super T> action);
    public CompletionStage<Void> thenAcceptAsync(Consumer<? super T> action);
    public CompletionStage<Void> thenRun(Runnable action);
    public CompletionStage<Void> thenRunAsync(Runnable action);
    public <U> CompletionStage<U> thenCompose(Function<? super T, ? extends CompletionStage<U>> fn);
    public <U> CompletionStage<U> thenComposeAsync(Function<? super T, ? extends CompletionStage<U>> fn);
    public CompletionStage<T> exceptionally(Function<Throwable, ? extends T> fn);
}
```

- 비동기적인 작업을 수행
- 해당 작업이 완료되면 결과를 처리하거나 다른 CompletionStage를 연결하는 인터페이스

- 50개에 가까운 연산자들을 활용하여 비동기 task들을 실행하고 값을 변형하는 등 chaining을 이용한 조합 가능
- 에러를 처리하기 위한 콜백 제공

```java
Helper.completionStage()
    .thenApplyAsync(value -> {
        log.info("thenApplyAsync: {}", value);
        return value + 1;
    }).thenAccept(value -> {
        log.info("thenAccept: {}", value);
    }).thenRunAsync(() -> {
        log.info("thenRun");
    }).exceptionally(e -> {
        log.info("exceptionally: {}", e.getMessage());
        return null;
    });
Thread.sleep(100);
```

ForkJoinPool - thread pool
- `CompletableFuture`, `completionStage`는 내부적으로 비동기 함수들을 실행하기 위해 ForkJoinPool을 사용
- ForkJoinPool의 기본 size = 할당된 cpu 코어 - 1 ex) 내 cpu가 10개면 9개가 기본할당됨.
- 데몬 쓰레드. main 쓰레드가 종료되면 즉각적으로 종료
- Task를 fork를 통해서 subtask로 나누고
- Thread pool에서 steal work 알고리즘을 이
용해서 균등하게 처리해서
- join을 통해서 결과를 생성


### ExecutorService

- 쓰레드 풀을 이용하여 비동기적으로 작업을 실행하고 관리
- 별도의 쓰레드를 생성하고 관리하지 않아도 되므로(알아서 관리됨), 코드를 간결하게 유지 가능
- 쓰레드 풀을 이용하여 자원을 효율적으로 관리

```java
public interface ExecutorService extends Executor {
    void execute(Runnable command);
    <T> Future<T> submit(Callable<T> task);
    void shutdown();
}
```

- execute: Runnable 인터페이스를 구현한 작업을 쓰레드 풀에서 비동기적으로 실행
- submit: Callable 인터페이스를 구현한 작업을 쓰레드 풀에서 비동기적으로 실행하고, 해당 작업의 결과를 Future<T> 객체로 반환
- shutdown: ExecutorService를 종료. 더 이상 task를 받지 않는다

### Executors - ExecutorService 생성

- `newSingleThreadExecutor`: 단일 쓰레드로 구성된 스레드 풀을 생성. 한 번에 하나의 작업만 실행
- `newFixedThreadPool`: 고정된 크기의 쓰레드 풀을 생성. 크기는 인자로 주어진 n과 동일
- `newCachedThreadPool`: 사용 가능한 쓰레드가 없다면 새로 생성해서 작업을 처리하고, 있다면 재사용. 쓰레드가 일정 시간 사용되지 않으면 회수
- `newScheduledThreadPool`: 스케줄링 기능을 갖춘 고정 크기의 쓰레드 풀을 생성. 주기적이거나 지연이 발생하는 작업을 실행
- `newWorkStealingPool`: work steal 알고리즘을 사용하는 ForkJoinPool을 생성
