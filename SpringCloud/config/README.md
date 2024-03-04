# SpringCloud - config

## spring cloud config
MSA에서  환경설정을 외부로 분리하여 관리할 수 있는 기능을 제공<br/>
Config Server를 사용하여 모든 환경(dev, test, prod)의 관리
운영중에 서버 빌드 및 배포 없이 환경설정 변경 가능덕션 등)에 대한 어플리케이션들의 속성을 한 곳에서 관리가능<br/>


![config](https://github.com/ydj515/record-study/assets/32935365/ecafa2c4-b10a-4633-8f21-d8dd352b444b)


#### server setup
- gradle
```gradle
    implementation 'org.springframework.cloud:spring-cloud-config-server'
    implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

- main
```java
@EnableConfigServer
@SpringBootApplication
public class ConfigApplication {

    public static void main(String[] args) {
        SpringApplication.run(ConfigApplication.class, args);
    }

}
```

- application.yml
`git url`은 default가 `main` branch 기준으로 읽음을 유의 <br/>

아래는 설정 파일을 spring cloud config server가 읽는 기준이다.<br/>
  - /{application}/{profile}[/{label}]
  - /{application}-{profile}.yml
  - /{label}/{application}-{profile}.yml
  - /{application}-{profile}.properties
  - /{label}/{application}-{profile}.properties

```yml
server:
  port: 8888

spring:
  application:
    name: config-service
  profiles:
    active: dev
  cloud:
    config:
      server:
        git:
          uri: file://dev/project/local-repo
#          search-paths: test-cloud-config-file/**
#          default-label: main
#          username: {username}
#          password: {password}

# actuator
management:
  endpoints:
    web:
      exposure:
        include: "*"
  info:
    env:
      enabled: true
```

아래와 같이 설정하면 file system에서 읽어오는 것 또한 가능하다.
```yml
spring:
  application:
    name: config-service
  profiles:
    active: native
  cloud:
    config:
      server:
        native:
          search-locations: file://${user.home}/dev/project/native-file-repo
```

private repository ssh로 접근도 가능하다.
```yml
spring:
  application:
    name: config-service
  profiles:
    active: dev
  cloud:
    config:
      server:
        git:
          uri: file://dev/project/local-repo
          default-label: main
          try-master-branch: false
          ignore-local-ssh-settings: true
          host-key: {someHostKey}
          host-key-algorithm: {ssh-rsa}
          private-key: {private key}
```

#### client setup

- application.yml
```yml
spring:
  profiles:
    active: dev
  cloud:
    config:
      name: ecommerce
  config:
    import: optional:configserver:http://localhost:8888

# actuator
management:
  endpoints:
    web:
      exposure:
        include: "*"
  info:
    env:
      enabled: true
```


- test
http://localhost:8888/{yml-file-name}/{profile}/default

```sh
curl http://localhost:8888/ecommerce/dev
```

[참조]<br/>
https://docs.spring.io/spring-cloud-config/docs/current/reference/html/<br/>
https://coe.gitbook.io/guide/config/springcloudconfig