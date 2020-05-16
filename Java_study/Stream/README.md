# Stream

## What is Stream
- <a href="https://github.com/backlo-study-programing/study-docs/blob/master/Java%20%EC%9E%90%EB%A3%8C/Stream%20%ED%99%9C%EC%9A%A9.md">참고 문서</a>
- 스트림은 **데이터의 흐름**
- 배열 또는 컬렉션 인스턴스에 함수 여러 개를 조합해서 원하는 결과를 필터링하고 가공된 결과를 얻을 수 있음
- **람다표현식**을 사용하여 가독성을 높히고, 간결하게 표현 가능 **->배열과 컬렉션을 함수형으로 처리할 수 있음**
- 간단하게 **병렬처리(multi-threading)**가 가능
- 쓰레드를 이용해 많은 요소들을 빠르게 처리할 수 있음
- Stream은 **재사용이 불가능** 하므로 다시 사용할 수 없음
- 병렬 스트림은 여러 쓰레드가 작업
- 간단한 예제 코드가 밑에 있다. 이처럼 **가독성**이 뛰어나고, 코드양을 줄일 수 있다

```java
// 원래 for문 방식
List<Integer> list = new ArrayList<Integer>();
        
for(int i=10;i<20;i++) {
    list.add(i);
}

int sum = 0;
Iterator<Integer> it = list.iterator();

while (it.hasNext()) {
    int num = it.next();
    if (num > 10) {
        sum += num;
    }
}
```

```java
// stream 사용 방식
// 원래 for문 방식
List<Integer> list = new ArrayList<Integer>();
        
for(int i=10;i<20;i++) {
    list.add(i);
}

int sum = 0;

sum = list.stream().filter(i -> i > 10).mapToInt(i -> i).sum();
```


## 스트림 사용하기
1. **스트림 생성**(스트림 인스턴스 생성)
2. **중개 연산**(필터링, 매핑하는 중간작업)
3. **최종 연산**(결과를 만들어내는 작업)

### 스트림 생성
```java
List<String> hororok = Arrays.asList("yoo", "dong", "jin", "jjang");
hororok.stream(); //Collection에서 스트림 생성
 
Double[] array = {3.1, 3.2, 3.3};
Arrays.stream(array);//배열로 스트림 생성
 
Stream<Integer> arr = Stream.of(1,2); // 스트림 직접 생성
```

#### 배열 스트림
```java
String[] Myarr = new String[]{"a", "b", "c"};
Stream<String> stream = Arrays.stream(Myarr); // Arrays.stream 메소드 사용
Stream<String> streamOfArrayPart = Arrays.stream(arr, 1, 3); // 1~2 요소 [b, c]
```

#### 컬렉션 스트림
```java
public interface Collection<E> extends Iterable<E> {
  default Stream<E> stream() {
    return StreamSupport.stream(spliterator(), false);
  }
}
List<String> list = Arrays.asList("a", "b", "c");
Stream<String> stream = list.stream();
Stream<String> parallelStream = list.parallelStream(); // 병렬 처리 스트림
```

### 중개 연산

#### filter
- 조건에 맞게 걸러줌
- **boolean 결과를 리턴하는 람다표현식이 필요!!**
```java
// list의 요소중에서 10보다 큰것만 누적
list.stream().filter(i -> i > 10).mapToInt(i -> i).sum();
```

```java
List<String> names = Arrays.asList("Eric", "Elena", "Java");
Stream<String> stream = names.stream().filter(name -> name.contains("a")); // [Elena, Java]
```

#### map
- 각 요소를 연산하는데 쓰임
- 입력 컬렉션을 mapping 하거나 변경
```java
// 각 문자열마다 뒤에 !를 붙힘
// 병렬 스트림도 사용
List<String> names = Arrays.asList("yoo", "dong", "jin", "jjang");
names.parallelStream().map((x) -> { return x.concat("!");} ).forEach(x -> System.out.println(x)); // yoo!, dong!, jin!, jjang!
```

```java
List<String> names = Arrays.asList("Eric", "Elena", "Java");
Stream<String> stream = names.stream().map(String::toUpperCase); // [ERIC, ELENA, JAVA]
```
- flatMap 이란것도 있는데 복잡하니까 찾아보고 나중에 할 예정 ㅎ_ㅎ

#### mapToInt, mapToDouble, MapToLong
- 각각 int, double, long 형태의 스트림으로 변환해줌
```java
list.stream().filter(i -> i > 10).mapToInt(i -> i).sum();
list.stream().filter(i -> i > 10).mapToDouble(i -> i).sum();
list.stream().filter(i -> i > 10).MapToLong(i -> i).sum();
```

#### peek
- map 과 유사
```java
int sum = IntStream.of(1, 3, 5, 7, 9).peek(System.out::println).sum();
```

#### sorted
- 스트림 요소를 정렬 시켜줌(default로는 오름차순)
```java
List<String> lang = Arrays.asList("Java", "Scala", "Groovy", "Python", "Go", "Swift");

// 기본으로 오름차순
lang.stream().sorted().collect(Collectors.toList()); // [Go, Groovy, Java, Python, Scala, Swift]

// 내림차순
lang.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList()); // [Swift, Scala, Python, Java, Groovy, Go]
```

#### limit
```java
// 스트림 갯수를 제한. 스트림형태로 반환
List<Integer> ages = Arrays.asList(1,2,3,4,5,6,7,8,9);
ages.stream().filter(x -> x>3)).limit(3); //4,5,6
```

#### distinct
- 중복 제거
```java
// 스트림 갯수를 제한. 스트림형태로 반환
List<Integer> ages = Arrays.asList(1,2,3,4,5,6,7,8,9);
ages.stream().filter(x -> x>3)).limit(3); //4,5,6
```

### 최종 연산

#### count
- 스트림의 갯수 연산
```java
long count = IntStream.of(1, 3, 5, 7, 9).count();
```

#### min
- 스트림에서 최솟값 추출
```java
OptionalInt min = IntStream.of(1, 3, 5, 7, 9).min();
```

#### max
- 스트림에서 최댓값 추출
```java
OptionalInt min = IntStream.of(1, 3, 5, 7, 9).max();
```

#### sum
- 스트림의 합 누적
```java
long sum = LongStream.of(1, 3, 5, 7, 9).sum();
```

### ifPresent
- 중개연산 말고도 최종연산에서도 if문식으로 걸를 수 있다
```java
DoubleStream.of(1.1, 2.2, 3.3, 4.4, 5.5).average().ifPresent(System.out::println);
```

#### reduce
- 누적된 값을 계산
```java
OptionalInt reduced = IntStream.range(1, 4) // [1, 2, 3]
  .reduce((a, b) -> {
    return Integer.sum(a, b); // 6(1+2+3)
  });)
```

```java
int reducedTwoParams = IntStream.range(1, 4) // [1, 2, 3]
  .reduce(10, Integer::sum); // 초기값:10 + 1 + 2 + 3 = 16
```

```java
List<Integer> ages = new ArrayList<Integer>();
ages.add(1);
ages.add(2);
ages.add(3);
System.out.println(ages.stream().reduce((b,c) -> b+c).get()); // 1+2+3=6
```

#### forEach
```java
List<Integer> ages = new ArrayList<Integer>();
ages.add(1);
ages.add(2);
ages.add(3);
Set<Integer> set = ages.stream().collect(Collectors.toSet());
set.forEach(x-> System.out.println(x)); // 1,2,3
```

#### collect(toMap, toSet, toList)
- 스트림의 값들을 모아주는 기능
- 각각 map, set, list 스트림으로 바꿔줌
```java 
Set<Integer> set = ages.stream().collect(Collectors.toList());
Set<Integer> set = ages.stream().collect(Collectors.toSet());

// String 요소에 대해 각 첫글자를 key로 가지는 map 만들기
Map<Character, String> map = list.stream().collect(Collectors.toMap(i -> i.charAt(0), i -> i));
```

#### iterator
- iterator로 반환
```java
List<String> names = Arrays.asList("yoo", "dong", "jin", "jjang");
Iterator<String> iter = names.stream().iterator();
while(iter.hasNext()) {
    System.out.println(iter.next()); // yoo, dong, jin, jjang
}
```

#### noneMatch, anyMatch, allMatch
- boolean을 표현하는 람다식 필요
```java
List<Integer> ages = new ArrayList<Integer>();
ages.add(1);
ages.add(2);
ages.add(3);
System.out.println(ages.stream().filter(x -> x > 1).noneMatch(x -> x > 2)); // false
```

## 주의사항
### **스트림은 재사용이 불가능**
- Stream 재사용 불가 stream has already been operated upon or closed.
```java
Stream<String> a = names.stream().filter(x -> x.contains("o"));
count = a.count();
        
List<String> lists = a.collect(Collectors.toList());
```

### **병렬 스트림은 여러 쓰레드가 작업**
- 여러개의 스레드가 필터링 하고 나온 요소 수를 계산하고 스레드 끼리 다시 각자 계산한 count 값을 더해서 리턴
- 오버헤드가 더 클 수 도 있으므로 무조건 성능면에서 유리한 것은 아님
```java
names.parallelStream().filter(x -> x.contains("o")).count();
```

### **중개연산은 미리 하지 않고 지연 연산을 함**
```java
Stream<String> a = names.stream().filter(x -> x.contains("o")).map(x-> x.concat("s"));
a.forEach(x -> System.out.println(x));
```

### filter와 map의 차이
- filter는 boolean을 처리하는 람다식이 필요, map은 입력 컬렉션을 mapping 하거나 변경

## 실전연습
### <a href="https://github.com/ydj515/record-study/blob/master/Java_study/Stream/src/traderAndTransaction/Main.java">문제풀이</a>
### <a href="https://github.com/ydj515/record-study/blob/master/Java_study/Stream/src/stringcalculator/StringAddCalculator.java">예제</a>
### <a href="https://github.com/ydj515/record-study/blob/master/Java_study/Stream/src/example/Main.java">예제</a>

[출처]  
https://jeong-pro.tistory.com/165  
https://futurecreator.github.io/2018/08/26/java-8-streams/  