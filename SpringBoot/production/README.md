# SpringBoot production
springboot production으로 올리면 관리할 수 있는 의존성 및 팁 추가

## actuator
actuator는 엔드포인트를 제공하는데, 인증 정보(누가 인증했고, 실패했고 등), 등록된 빈, 어떤 자동설정이 어떤 조건에 대해 적용되었는지, flyway, 최근 100개의 요청 등 여러가지 정보를 얻을 수 있음(hateoas 형태로 제공)<br/>
http를 사용할 경우는 health, info만 제공<br/>
endpoint 직접 조작 시 아래와 같이 설정(https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#actuator.endpoints)
```yml
management:
  endpoints:
    필요기능:
      enabled: true / false
```
공개여부는 아래와 같이 설정
```yml
management:
  endpoints:
    web:
      exposure:
        include: "*"
```

#### pom.xml
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

#### http://localhost:8080/actuator
`/actuator` 경로로 접근 시 아래와 같은 응답을 hateoas 형태로 받을 수 있다.(endpoint를 전부 open 하는 yml 설정 하지 않으면 health, info만 제공)
```json
// 20240208200041
// http://localhost:8080/actuator

{
  "_links": {
    "self": {
      "href": "http://localhost:8080/actuator",
      "templated": false
    },
    "beans": {
      "href": "http://localhost:8080/actuator/beans",
      "templated": false
    },
    "caches-cache": {
      "href": "http://localhost:8080/actuator/caches/{cache}",
      "templated": true
    },
    "caches": {
      "href": "http://localhost:8080/actuator/caches",
      "templated": false
    },
    "health": {
      "href": "http://localhost:8080/actuator/health",
      "templated": false
    },
    "health-path": {
      "href": "http://localhost:8080/actuator/health/{*path}",
      "templated": true
    },
    "info": {
      "href": "http://localhost:8080/actuator/info",
      "templated": false
    },
    "conditions": {
      "href": "http://localhost:8080/actuator/conditions",
      "templated": false
    },
    "configprops": {
      "href": "http://localhost:8080/actuator/configprops",
      "templated": false
    },
    "configprops-prefix": {
      "href": "http://localhost:8080/actuator/configprops/{prefix}",
      "templated": true
    },
    "env": {
      "href": "http://localhost:8080/actuator/env",
      "templated": false
    },
    "env-toMatch": {
      "href": "http://localhost:8080/actuator/env/{toMatch}",
      "templated": true
    },
    "flyway": {
      "href": "http://localhost:8080/actuator/flyway",
      "templated": false
    },
    "loggers": {
      "href": "http://localhost:8080/actuator/loggers",
      "templated": false
    },
    "loggers-name": {
      "href": "http://localhost:8080/actuator/loggers/{name}",
      "templated": true
    },
    "heapdump": {
      "href": "http://localhost:8080/actuator/heapdump",
      "templated": false
    },
    "threaddump": {
      "href": "http://localhost:8080/actuator/threaddump",
      "templated": false
    },
    "metrics-requiredMetricName": {
      "href": "http://localhost:8080/actuator/metrics/{requiredMetricName}",
      "templated": true
    },
    "metrics": {
      "href": "http://localhost:8080/actuator/metrics",
      "templated": false
    },
    "quartz": {
      "href": "http://localhost:8080/actuator/quartz",
      "templated": false
    },
    "quartz-jobsOrTriggers": {
      "href": "http://localhost:8080/actuator/quartz/{jobsOrTriggers}",
      "templated": true
    },
    "quartz-jobsOrTriggers-group": {
      "href": "http://localhost:8080/actuator/quartz/{jobsOrTriggers}/{group}",
      "templated": true
    },
    "quartz-jobsOrTriggers-group-name": {
      "href": "http://localhost:8080/actuator/quartz/{jobsOrTriggers}/{group}/{name}",
      "templated": true
    },
    "scheduledtasks": {
      "href": "http://localhost:8080/actuator/scheduledtasks",
      "templated": false
    },
    "mappings": {
      "href": "http://localhost:8080/actuator/mappings",
      "templated": false
    },
    "refresh": {
      "href": "http://localhost:8080/actuator/refresh",
      "templated": false
    },
    "features": {
      "href": "http://localhost:8080/actuator/features",
      "templated": false
    }
  }
}
```

## JMX
terminal 창 하나 킨 후 `jconsole`입력<br/>
프로젝트 클릭한 후 connect, Insecure connection<br/>
Heap memory 사용량, thread 갯수, 로딩한 class 갯수 CPU 사용량 등 watch 기능

![jconsole1](https://github.com/ydj515/record-study/assets/32935365/38b4b3ab-7029-488f-a265-173529e193c0)

![jconsole](https://github.com/ydj515/record-study/assets/32935365/bd15c27a-1d0d-4ece-a295-15940f324ae2)




## admin
Actuator 정보를 UI로 볼 수 있음(3rd party 제품)<br/>
server를 담당하는 application 1개와 n개의 client application으로 구성<br/>

#### server
- 아래의 의존성 주입
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-server</artifactId>
    <version>3.0.2</version>
</dependency>
```

- main class에 어노테이션 추가
```java
@SpringBootApplication
@EnableAdminServer
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

}
```

- server port 설정
```yml
server:
  port: 18080
```

#### client
- 아래의 의존성 주입
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>de.codecentric</groupId>
    <artifactId>spring-boot-admin-starter-client</artifactId>
    <version>3.0.2</version>
</dependency>
```

- application.yml
yml에 아래 내용 추가
```yml
server:
  port: 8080

# actuator config
management:
  endpoints:
    web:
      exposure:
        include: "*"
  info:
    env:
      enabled: true

# master server info
spring:
  boot:
    admin:
      client:
        url: "http://localhost:18080"
        instance:
          service-url: "http://localhost:8080"
```

#### 확인
server url로 설정해놓은 localhost:18080으로 접속하면 아래와 같은 화면이 나온다.<br/>
n개의 client server들의 정보를 확인할 수 있다.
![admin1](https://github.com/ydj515/record-study/assets/32935365/b39ac6be-a591-4fda-988b-38cec1ec26d3)

![admin2](https://github.com/ydj515/record-study/assets/32935365/1cd5d6ce-c19d-401d-aaa9-b72acd4d58ff)





[출처]<br/>
https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#actuator.endpoints