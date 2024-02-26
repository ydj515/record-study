# SpringCloud - gateway
![spring cloud gateway](https://github.com/ydj515/record-study/assets/32935365/45a39269-c2d3-42b4-9f01-c3e1f58a15df)

## spring cloud gateway
|                |Spring cloud Gateway                          |Netflix Zuul                         |
|----------------|-------------------------------|-----------------------------|
|`동작방식`          |비동기|동기|
|`동작원리`          |Predicates+Filters| filter only|
|`사용 서버`          |netty|servlet MVC, tomcat|

![zuul](https://github.com/ydj515/record-study/assets/32935365/3f2275eb-af2c-4357-ab3c-1f1b1a28ecc4)

![spring cloud gateway kakao](https://github.com/ydj515/record-study/assets/32935365/a15a581d-dc21-4703-a477-57a3174b6eb2)


말그대로 gateway 방식.<br/>
gateway service에는 `gateway-mvc, eureka-client`를 추가. 라우팅 되는 서비스는 `web, eureka-client, lombok`을 추가하여 테스트 진행

```gradle
    implementation 'org.springframework.boot:spring-boot-starter-webflux'
    implementation 'org.springframework.cloud:spring-cloud-starter-gateway'
    implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'io.projectreactor:reactor-test'
```
## 1. routing
#### gateway service
다음과 같이 `application.yml`파일을 작성한다.

- application.yml
```yml
server:
  port: 8080

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://localhost:8761/eureka

spring:
  application:
    name: api-gateway-service
  cloud:
    gateway:
      mvc:
        routes:
          - id: first-service
            uri: http://localhost:8081/
            predicates:
              - Path=/first-service/**
          - id: second-service
            uri: http://localhost:8082/
            predicates:
              - Path=/second-service/**
```


#### first service
controller와 yml 파일 작성
- controller
```java
@RestController
@RequestMapping("/first-service")
public class FirstServiceController {

    @GetMapping("/welcome")
    public String welcome() {
        return "first service";
    }

}
```
- application.yml
```yml
server:
  port: 8081

spring:
  application:
    name: first-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```

#### second service
controller와 yml 파일 작성
- controller
```java
@RestController
@RequestMapping("/second-service")
public class SecondServiceController {

    @GetMapping("/welcome")
    public String welcome() {
        return "second service";
    }

}
```

- application.yml
```yml
server:
  port: 8082

spring:
  application:
    name: second-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```

#### test
`gateway service`의 application.yml 파일을 보면

- `localhost:8080/second-service/welcome` => second-service의 welcome으로 매핑되는걸 확인할 수 있다.
- `localhost:8080/first-service/welcome` => first-service의 welcome으로 매핑되는걸 확인할 수 있다.




## 2. filter
#### gateway service
간단하게 filter를 적용하면서 request, response parameter에 추가하여 routing하는 방법.<br/>
다음과 같이 `application.yml`파일을 작성한다.

- application.yml
```yml
server:
  port: 8080

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://localhost:8761/eureka

spring:
  application:
    name: api-gateway-service
  cloud:
    gateway:
      routes:
        - id: first-service
          uri: http://localhost:8081
          predicates:
            - Path=/first-service/**
          filters:
            - AddRequestHeader=first-request, first-request-header2 # FilterConfig와 같은 의미. (앞에가 key, 뒤에가 value)
            - AddResponseHeader=first-response, first-response-header2
        - id: second-service
          uri: http://localhost:8082
          predicates:
            - Path=/second-service/**
          filters:
            - AddRequestHeader=second-request, second-request-header2 # FilterConfig와 같은 의미. (앞에가 key, 뒤에가 value)
            - AddResponseHeader=second-response, second-response-header2
```

- FilterConfig
`application.yml`과 같은 설정을 java config로 설정하면 아래와 같다.
```java
@Configuration
@Slf4j
public class FilterConfig {

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder) {
        return builder.routes()
                .route(r -> r.path("/first-service/**")
                        .filters(f -> f.addRequestHeader("first-request", "first-request-header")
                                .addResponseHeader("first-response", "first-response-header"))
                        .uri("http://localhost:8081"))
                .route(r -> r.path("/second-service/**")
                        .filters(f -> f.addRequestHeader("second-request", "second-request-header")
                                .addResponseHeader("second-response", "second-response-header"))
                        .uri("http://localhost:8082"))
                .build();
    }
}
```

<strong> 자세한 필터를 더 추가하기 위해 아래와 같이 `application.yml`을 변경하고 filter를 추가하여 진행한다.</strong> <br/>

- application.yml
```yml
server:
  port: 8080

eureka:
  client:
    register-with-eureka: false
    fetch-registry: false
    service-url:
      defaultZone: http://localhost:8761/eureka

spring:
  application:
    name: api-gateway-service
  cloud:
    gateway:
      default-filters:
        - name: GlobalFilter
          args:
            baseMessage: spring cloud gateway global filter
            preLogger: true
            postLogger: true
      routes:
        - id: first-service
          uri: http://localhost:8081
          predicates:
            - Path=/first-service/**
          filters:
            - CustomFilter
#            - AddRequestHeader=first-request, first-request-header2 # FilterConfig와 같은 의미. (앞에가 key, 뒤에가 value)
#            - AddResponseHeader=first-response, first-response-header2
        - id: second-service
          uri: http://localhost:8082
          predicates:
            - Path=/second-service/**
          filters:
#            - AddRequestHeader=second-request, second-request-header2 # FilterConfig와 같은 의미. (앞에가 key, 뒤에가 value)
#            - AddResponseHeader=second-response, second-response-header2
            - name: CustomFilter
            - name: LoggingFilter
              args:
                baseMessage: spring cloud gateway global filter
                preLogger: true
                postLogger: true
```

- CustomFilter
```java
@Component
@Slf4j
public class CustomFilter extends AbstractGatewayFilterFactory<CustomFilter.Config> {
    public CustomFilter() {
        super(Config.class);
    }

    @Override
    public GatewayFilter apply(Config config) {
        System.out.println("========================custom filter");
        //Custom Pre Filter
        return (exchange, chain) -> {
            ServerHttpRequest request = exchange.getRequest();
            ServerHttpResponse response = exchange.getResponse();

            log.info("Custom Pre filter: request id -> {}", request.getId());

            //Custom Post Filter
            return chain.filter(exchange).then(Mono.fromRunnable(() -> {
                log.info("Custom Post filter: response code -> {}", response.getStatusCode());
            }));
        };
    }

    public static class Config {
        //Put the configuration properties
    }
}
```

- GlobalFilter
```java
@Component
@Slf4j
public class GlobalFilter extends AbstractGatewayFilterFactory<GlobalFilter.Config> {
    public GlobalFilter() {
        super(Config.class);
    }

    @Override
    public GatewayFilter apply(Config config) {
        System.out.println("========================global filter");
        //Custom Pre Filter
        return (exchange, chain) -> {
            ServerHttpRequest request = exchange.getRequest();
            ServerHttpResponse response = exchange.getResponse();
            log.info("Global Filter baseMessage: -> {}", config.getBaseMessage());

            if (config.isPreLogger()) log.info("Global Filter Start: request id -> {}", request.getId());
            //Custom Post Filter
            return chain.filter(exchange).then(Mono.fromRunnable(() -> {
                if (config.isPostLogger())
                    log.info("Global Filter End: response status code -> {}", response.getStatusCode());
            }));
        };
    }

    @Data
    public static class Config {
        private String baseMessage;
        private boolean preLogger;
        private boolean postLogger;
    }
}
```

- LoggingFilter
```java
@Component
@Slf4j
public class LoggingFilter extends AbstractGatewayFilterFactory<LoggingFilter.Config> {
    public LoggingFilter() {
        super(Config.class);
    }

    @Override
    public GatewayFilter apply(Config config) {

        return new OrderedGatewayFilter((exchange, chain) -> {
            System.out.println("========================logging filter");
            ServerHttpRequest request = exchange.getRequest();
            ServerHttpResponse response = exchange.getResponse();
            log.info("Logging Filter baseMessage: -> {}", config.getBaseMessage());

            if (config.isPreLogger()) log.info("Logging Filter Start: request id -> {}", request.getId());
            //Custom Post Filter
            return chain.filter(exchange).then(Mono.fromRunnable(() -> {
                if (config.isPostLogger())
                    log.info("Logging Filter End: response status code -> {}", response.getStatusCode());
            }));
        }, Ordered.LOWEST_PRECEDENCE);//제일 낮은 순위로 필터를 적용
    }

    @Data
    public static class Config {
        private String baseMessage;
        private boolean preLogger;
        private boolean postLogger;
    }
}
```


#### first service
controller와 yml 파일 작성
- controller
```java
@Slf4j
@RestController
@RequestMapping("/first-service")
public class FirstServiceController {

    @GetMapping("/welcome")
    public String welcome() {
        return "first service";
    }

    @GetMapping("/message")
    public String message(@RequestHeader("first-request") String header) {
        log.info(header);
        return "Welcome to the First service.";
    }

    @GetMapping("/check")
    public String check() {
        return "Hi, there. This is a message from First Service";
    }

}
```
- application.yml
```yml
server:
  port: 8081

spring:
  application:
    name: first-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```

#### second service
controller와 yml 파일 작성
- controller
```java
@Slf4j
@RestController
@RequestMapping("/second-service")
public class SecondServiceController {

    @GetMapping("/welcome")
    public String welcome() {
        return "second service";
    }

    @GetMapping("/message")
    public String message(@RequestHeader("second-request") String header) {
        log.info(header);
        return "Welcome to the Second service.";
    }

    @GetMapping("/check")
    public String check() {
        return "Hi, there. This is a message from Second Service";
    }

}
```

- application.yml
```yml
server:
  port: 8082

spring:
  application:
    name: first-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```

#### test
- `http://localhost:8080/first-service/check`
request -> default-filters(GlobalFilter) -> filters(CustomFilter) -> first service -> filters(CustomFilter) -> default-filters(GlobalFilter) -> response<br/>
![first](https://github.com/ydj515/record-study/assets/32935365/8bae30f4-ea90-4eb6-86fb-f3ddf55d9ff5)


- `http://localhost:8080/second-service/check`
request -> default-filters(GlobalFilter) -> filters(CustomFilter) -> filters(LogingFilter)-> second service -> filters(LogingFilter) ->  filters(CustomFilter) -> default-filters(GlobalFilter) -> response<br/>
![second](https://github.com/ydj515/record-study/assets/32935365/eac04fc6-fdfe-4e10-a7c1-24112ca75525)



## 3. load balancing
#### discovery serivce(eureka server)
eureka client를 등록하기 위한 eureka server를 하나 기동 <br/>
first-service, second-service는 각각 2개를 기동<br/>

- gradle
```gradle
	implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-server'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
```

- application.yml
```yml
server:
  port: 8761

spring:
  application:
    name: discovery-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```

- main
```java
@SpringBootApplication
@EnableEurekaServer
public class DiscoveryServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(DiscoveryServiceApplication.class, args);
    }

}
```

#### first service
controller와 yml 파일 작성
- controller
```java
@Slf4j
@RestController
@RequestMapping("/first-service")
public class FirstServiceController {

    @GetMapping("/welcome")
    public String welcome() {
        return "first service";
    }

    @GetMapping("/message")
    public String message(@RequestHeader("first-request") String header) {
        log.info(header);
        return "Welcome to the First service.";
    }

    @GetMapping("/check")
    public String check() {
        return "Hi, there. This is a message from First Service";
    }

}
```
- application.yml
```yml
server:
  port: 8081

spring:
  application:
    name: first-service

eureka:
  client:
    fetch-registry: false
    register-with-eureka: false
```


#### first service
controller와 yml 파일 작성
- controller
```java
@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/first-service")
public class FirstServiceController {

    private final Environment env;

    @GetMapping("/check")
    public String check(HttpServletRequest request) {
        log.info("check is called in First Service");
        log.info("Server Port from HttpServletRequest: port = {}", request.getServerPort());
        log.info("Server Port from Environment: port = {}", env.getProperty("local.server.port"));

        return String.format("check is called in First Service, Server port is %s from HttpServletRequest and %s from Environment", request.getServerPort(), env.getProperty("local.server.port"));
    }

}
```

- application.yml
```yml
server:
  port: 0

spring:
  application:
    name: first-service

eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: http://localhost:8761/eureka
  instance:
    instance-id: ${spring.application.name}:${spring.application.instance_id:${random.value}}
```


#### second service
controller와 yml 파일 작성
- controller
```java
@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/second-service")
public class SecondServiceController {

    private final Environment env;

    @GetMapping("/check")
    public String check(HttpServletRequest request) {
        log.info("check is called in Second Service");
        log.info("Server Port from HttpServletRequest: port = {}", request.getServerPort());
        log.info("Server Port from Environment: port = {}", env.getProperty("local.server.port"));

        return String.format("check is called in First Service, Server port is %s from HttpServletRequest and %s from Environment", request.getServerPort(), env.getProperty("local.server.port"));
    }

}
```

- application.yml
```yml
server:
  port: 0

spring:
  application:
    name: second-service

eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: http://localhost:8761/eureka
  instance:
    instance-id: ${spring.application.name}:${spring.application.instance_id:${random.value}}
```

#### api gateway
- application.yml
`http://{ip}:{port}` 였던 부분을 eruaka server에 등록되어있는 `lb://{springApplicationName}` 으로 변경
```yml
server:
  port: 8080

eureka:
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: http://localhost:8761/eureka

spring:
  application:
    name: api-gateway-service
  cloud:
    gateway:
      default-filters:
        - name: GlobalFilter
          args:
            baseMessage: spring cloud gateway global filter
            preLogger: true
            postLogger: true
      routes:
        - id: first-service
#          uri: http://localhost:8081
          uri: lb://FIRST-SERVICE
          predicates:
            - Path=/first-service/**
        - id: second-service
#          uri: http://localhost:8082
          uri: lb://SECOND-SERVICE
          predicates:
            - Path=/second-service/**
```
![eurekaserver](https://github.com/ydj515/record-study/assets/32935365/beaa4c2f-d5e6-4b9c-9753-6b53a09c09ad)


#### test
각각 first-service, second-service로 요청을 보내면 round robbin 정책에 의해 loadbalnacing되어서 request를 전달.




[참조]<br/>
https://www.slideshare.net/ifkakao/msa-api-gateway