# SpringBoot - AOP
Aspect Oriented Programming

```
Aspect : 위에서 설명한 흩어진 관심사를 모듈화 한 것
Target : Aspect를 적용하는 곳 (클래스, 메서드 .. )
Advice : 실질적으로 어떤 일을 해야할 지에 대한 것, 실질적인 부가기능을 담은 구현체
JointPoint : Advice가 적용될 위치, 끼어들 수 있는 지점. 메서드 진입 지점, 생성자 호출 시점, 필드에서 값을 꺼내올 때 등 다양한 시점에 적용
PointCut : JointPoint의 상세한 스펙을 정의한 것. 'A란 메서드의 진입 시점에 호출할 것'과 같이 더욱 구체적으로 Advice가 실행될 지점 지정
```

```
@Before (이전) : 어드바이스 타겟 메소드가 호출되기 전에 어드바이스 기능을 수행
@After (이후) : 타겟 메소드의 결과에 관계없이(즉 성공, 예외 관계없이) 타겟 메소드가 완료 되면 어드바이스 기능을 수행
@AfterReturning (정상적 반환 이후)타겟 메소드가 성공적으로 결과값을 반환 후에 어드바이스 기능을 수행
@AfterThrowing (예외 발생 이후) : 타겟 메소드가 수행 중 예외를 던지게 되면 어드바이스 기능을 수행
@Around (메소드 실행 전후) : 어드바이스가 타겟 메소드를 감싸서 타겟 메소드 호출전과 후에 어드바이스 기능을 수행
```

- pom.xml
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
```

- PerfAspect.java
```java
@Component
@Aspect
public class PerfAspect {

    @Around("execution(* kr.go.aaa.collector.controller.*.*(..))")
    public Object logging(ProceedingJoinPoint pjp) throws Throwable {
        long startTime = System.currentTimeMillis();
        log.info("========== [start ] - class[{}] / method[{}]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName());
        Object result = pjp.proceed();
        log.info("========== [finish] - class[{}] / method[{}] / time[{} sec]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName(), (System.currentTimeMillis() - startTime) / 1000);
        return result;
    }
}
```

- EventService.java
```java
public interface EventService {

    void createEvent();

    void publishEvent();

    void deleteEvent();
}
```

- SimpleEventService.java
```java
@Component
public class SimpleEventService implements EventService {

    @Override
    public void createEvent() {
        try {
            Thread.sleep(1000);
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Created an event");
    }

    @Override
    public void publishEvent() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e){
            e.printStackTrace();;
        }
        System.out.println("Published an event");
    }

    @Override
    public void deleteEvent() {
        System.out.println("Delete an event");
    }
}
```


## Annotation

- PerLogging.java
```java
@Documented
@Target(ElementType.METHOD)
@Rentention(RententionPolicy.CLASS) // RententionPolicy.SOURCE로 하면 안됨. 반드시 주의. CLASS가 default
public @interface PerLogging {

}
```

- SimpleEventService.java
```java
@Component
public class SimpleEventService implements EventService {

    @Override
    @PerLogging
    public void createEvent() {
        try {
            Thread.sleep(1000);
        } catch(InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Created an event");
    }

    @Override
    @PerLogging
    public void publishEvent() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e){
            e.printStackTrace();;
        }
        System.out.println("Published an event");
    }

    @Override
    public void deleteEvent() {
        System.out.println("Delete an event");
    }
}
```

- PerfAspect.java
annotation 설정으로 변경
```java
@Component
@Aspect
public class PerfAspect {

    @Around("@annotation(PerLogging)")
    public Object logging(ProceedingJoinPoint pjp) throws Throwable {
        long startTime = System.currentTimeMillis();
        log.info("========== [start ] - class[{}] / method[{}]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName());
        Object result = pjp.proceed();
        log.info("========== [finish] - class[{}] / method[{}] / time[{} sec]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName(), (System.currentTimeMillis() - startTime) / 1000);
        return result;
    }
}
```

## Bean
- PerfAspect.java
해당 bean의 public method 지정
```java
@Component
@Aspect
public class PerfAspect {

    @Around("bean(simpleEventService)")
    public Object logging(ProceedingJoinPoint pjp) throws Throwable {
        long startTime = System.currentTimeMillis();
        log.info("========== [start ] - class[{}] / method[{}]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName());
        Object result = pjp.proceed();
        log.info("========== [finish] - class[{}] / method[{}] / time[{} sec]", pjp.getSignature().getDeclaringTypeName(), pjp.getSignature().getName(), (System.currentTimeMillis() - startTime) / 1000);
        return result;
    }
}
```