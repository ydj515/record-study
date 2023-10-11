# SpringBoot - scope

### singleton scope
동일한 인스턴스

- Single.java
```java
@Component
public class Single {
 
    @Autowired
    private Proto proto;
 
    public Proto getProto() {
        return proto;
    }
}
```

- Proto.java
```java
@Component
    public class Proto {
}
```

- AppRunner.java
```java
@Component
public class AppRunner implements ApplicationRunner {
 
    @Autowired
    Single single;
 
    @Autowired
    Proto proto;
 
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println(proto); // A
        System.out.println(single.getProto()); // A
    }
}
```

### prototype scope
생성할 때마다 인스턴스 생성

- Proto.java
```java
@Component @Scope("prototype")
    public class Proto {
}
```

- AppRunner.java
```java
@Component
public class AppRunner implements ApplicationRunner {
 
    @Autowired
    Single single;
 
    @Autowired
    Proto proto;
 
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("Proto:");
        System.out.println(ctx.getBean(Proto.class)); // A
        System.out.println(ctx.getBean(Proto.class)); // B
        System.out.println(ctx.getBean(Proto.class)); // C
 
        System.out.println("Single:");
        System.out.println(ctx.getBean(Single.class)); // D
        System.out.println(ctx.getBean(Single.class)); // D
        System.out.println(ctx.getBean(Single.class)); // D
    }
}
```

### 프로토 타입 빈에서 싱글톤 빈 참조
아무 문제 X

- Proto.java
```java
@Component @Scope("prototype")
public class Proto {
    
    @Autowired
    Single single;
}
```


### 싱글톤 타입 빈에서 프로토 빈 참조
문제 O

- Proto.java
```java
@Component
public class AppRunner implements ApplicationRunner {
 
    @Autowired
    ApplicationContext ctx;
 
    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("Proto:");
        System.out.println(ctx.getBean(Proto.class)); // A
        System.out.println(ctx.getBean(Proto.class)); // B
        System.out.println(ctx.getBean(Proto.class)); // C
 
        System.out.println("Single:");
        System.out.println(ctx.getBean(Single.class)); // D
        System.out.println(ctx.getBean(Single.class)); // D
        System.out.println(ctx.getBean(Single.class)); // D
 
        System.out.println("Proto by Single:");
        System.out.println(ctx.getBean(Single.class).getProto()); // E
        System.out.println(ctx.getBean(Single.class).getProto()); // E
        System.out.println(ctx.getBean(Single.class).getProto()); // E
    }
}
```

#### 해결방법1
proxy mode 설정.
원래 JDK 안에 있는 dynamic proxy는 인터페이스의 프록시만 만들 수 있기 때문에 클래스의 프록시는 써드 파티 라이브러리를 사용.
proto를 감싼 proxy를 사용하여 새로운 인스턴스를 생성

> scopedProxyMode.DEFAULT : Proxy를 사용하지 않음
> scopedProxyMode.TARGET_CLASS : Proxy를 사용함(클래스)
> scopedProxyMode.INTERFACES : Proxy를 사용함(인터페이스)

![proxy](https://github.com/ydj515/board/assets/32935365/ad4b9edb-4067-4ae3-b7ae-a1c820c3b664)



- Proto.java
```java
@Component @Scope(scopeName = "prototype", proxyMode = ScopedProxyMode.TARGET_CLASS)
    public class Proto {
}
```

#### 해결방법2

- Proto.java
```java
@Component @Scope(scopeName = "prototype")
    public class Proto {
}
```

- Single.java
```java
@Component
public class Single {
 
    @Autowired
    private ObjectProvider<Proto> proto;
 
    public Proto getProto() {
        return proto.getIfAvailable();
    }
}
```