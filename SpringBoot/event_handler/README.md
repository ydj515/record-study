# SpringBoot - event handler

spring 4.2 이상부터 spring code를 상속 받지 않는 POJO형태가 됨.
spring code가 개발자 코드에 침투하지 않는 철학을 녹임(비침투성)

### AS-IS
- MyEvent.java
```java
public class MyEvent extends ApplicationEvent {
 
    private int data;
 
    public MyEvent(Object source) {
        super(source);
    }

    public MyEvent(Object source, Clock clock) {
        super(source, clock);
    }

    public MyEvent(Object source, int data) {
        super(source);
        this.data = data;
    }
 
    public int getData() {
        return data;
    }
}
```

- AppRunner.java
```java
@Component
public class AppRunner implements ApplicationRunner {
 
    @Autowired
    ApplicationEventPublisher eventPublisher;
 
    @Override
    public void run(ApplicationArguments args) throws Exception {
        eventPublisher.publishEvent(new MyEvent(this, 100)); // event publish
    }
}
```

- MyEventHandler
```java
@Component
public class MyEventHandler implements ApplicationListener<MyEvent> {
    
    @Override
    public void onApplicationEvent(MyEvent event) {
        System.out.println("First event handling, data: " + event.getData());
    }
}
```

### TO-BE
- MyEvent.java
```java
public class MyEvent {

    private Object source;
    private int data;
 
    public MyEvent(Object source) {
        this(source, 0);
    }
 
    public MyEvent(Object source, int data) {
        this.source = source;
        this.data = data;
    }
 
    public Object getSource() {
        return source;
    }
 
    public int getData() {
        return data;
    }
}
```

- MyEventHandler
```java
@Component
public class MyEventHandler {
 
    @EventListener // event handler에 등록
    public void onMyEvent(MyEvent event) {
        System.out.println("First event handling, data: " + event.getData());
    }
}
```

### multi handler
이벤트 핸들러가 여러개일 경우 하나의 thread에서 순차적으로 실행(동시에 실행하지 않음.)
**순서를 주고 싶으면 @Order 사용**(값이 작을 수록 우선순위가 높음)
**다른 스레드에서 동시로 사용하고 싶으면 @Async 사용**(순서보장 x)

- MyEventHandler.java
```java
@Component
public class MyEventHandler {
 
    @EventListener
    @Order(Ordered.HIGHEST_PRECEDENCE)
    public void onMyEvent(MyEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("First event handling, data: " + event.getData());
    }
}
```

- AnotherEventHandler.java
```java
@Component
public class AnotherEventHandler {
 
    @EventListener
    @Order(Ordered.HIGHEST_PRECEDENCE + 2)
    public void onMyEvent(MyEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("Another event handling, data: " + event.getData());
    }
}
```


#### asnyc
순서 보장 x

- MyEventHandler.java
```java
@Component
public class MyEventHandler {
 
    @EventListener
    @Async
    public void onMyEvent(MyEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("First event handling, data: " + event.getData());
    }
}
```

- AnotherEventHandler.java
```java
@Component
public class AnotherEventHandler {
 
    @EventListener
    @Async
    public void onMyEvent(MyEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("Another event handling, data: " + event.getData());
    }
}
```

- MyApplication.java
EnableAsync 추가
```java
@SpringBootApplication
@EnableAsync
public class MyApplication {
 
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```


### spring 제공 event
- spring이 제공하는 event

|event          |description                   |
|------------------|-------------------------------|
|ContextRefresedEvent    |ApplicationContext를 초기화하거나 refresh할 때 발생                  |
|ContextStartedEvent       |ApplicationContext를 start()하여 라이프 사이클 빈들이 시작 신호를 받은 시점에 발생                    |
|ContextStoppedEvent           |ApplicationContext를 stop()하여 라이프 사이클 빈들이 정지 신호를 받은 시점에 발생             |
|ContextClosedEvent        |ApplicationContext를 stop()하여 라이프 사이클 빈들이 정지 신호를 받은 시점에 발생                    |
|RequestHandledEvent     |HTTP 요청을 처리했을 때 발생                  |


```java
@Component
public class MyEventHandler{
 
    @EventListener
    @Async
    public void onMyEvent(MyEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("First event handling, data: " + event.getData());
    }
 
    @EventListener
    @Async
    public void onContextRefreshedEvent(ContextRefreshedEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("ContextRefreshedEvent");
    }
 
    @EventListener
    @Async
    public void onContextClosedEvent(ContextClosedEvent event) {
        System.out.println(Thread.currentThread().toString());
        System.out.println("ContextClosedEvent");
    }
}

```