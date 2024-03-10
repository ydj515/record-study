# SpringCloud - config

## spring cloud config
![refresh](https://github.com/ydj515/record-study/assets/32935365/aa7605c7-e5b4-487a-b227-d779c8074766)
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
기본적으로 `application.yml` 파일도 읽어옴. (예를 들어서 dev 를 성정하더라도 설정값은 `application.yml`, `{application}-dev.yml` 이렇게 2개를 가져온다.)

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

- sample code
```java
@Component
@RefreshScope // 추가
@Sl4j
public class Service {
  @Value("${data-dam.url}")
  private String dataDamUrl;

  @Value("${config.elasticsearch.shard}")
  private int shard; // final keyword 제거. value는 contextload될때 값을 주입 받기때문에 @RefreshScope와 같이사용해야함
  @Value("${config.elasticsearch.replica}")
  private int replica;

  @PostConstruct
  public void initConstructor() {

    ApiLifecycleRequestModel apiLifecycleRequestModel = ApiLifecycleRequestModel.builder()
        .deleteMinAge(deleteMinAge)
        .build();

    // life cycle 등록
    String uri = dataDamUrl + CREATE_LIFECYCLE_API_PATH + "?" + RequestUtils.objectToQueryParam(apiLifecycleRequestModel);

    try {
      String response = webClientHelper.put(URI.create(uri), "");

      log.debug("Create Lifecycle : {}", response);
    } catch (Exception e) {
      log.error(e.getMessage());
    }

  }

  @EventListener(RefreshScopeRefreshedEvent.class)
  public void onRefresh(RefreshScopeRefreshedEvent event) {
    log.info("onRefresh event");
  }

}
```

`@RefreshScopee`와 `final` 키워드에 유의해서 코드를 작성해야한다.<br/>
`Environment`는 런타임에 변경될 수 있어서 @RefreshScope를 사용하지 않아도 됨<br/>
spring cloud는 RefreshEvent를 사용<br/>
변경된 정보는 @ConfigurationProperties, @RefreshScope 두가지 방식으로 전파<br/>
동시 접근 시 일관된 상태가 필요하면 @ConfigurationProperties, 아니라면 @RefreshScope를 사용<br/>
만일 @ConfigurationProperties에 @RefreshScope을 붙이면 @RefreshScope붙은 Bean과 같은 동작을 함<br/>

- @RefreshScope
@RefreshScope가 있는 bean은 proxy bean으로 생성<br/>
실제 bean은 시작시점에 생성되고 동일한 빈 이름을 가진 키로 캐쉬에 저장<br/>
메소드가 프록시를 호추러할 때 대상 빈으로 전파<br/>
EnvironmentChangeEvent가 발생하면 캐쉬는 초기화 되고 BeanFactory callback이 호출된 다음 메소드 호출시 재생성됨<br/>
@RefreshScope이 붙은 Bean은 프록시(proxy)로 생성이 되고 실제 Bean을 캐쉬에 저장<br/>
`/refresh`될 때 Proxy의 Bean이 destroy되고 캐쉬의 값이 초기화된다. 그리고 해당 컴포넌트가 실제로 호출될 때 생성(construct)된다.</br>

- ConfigurationProperties
`/refresh`될 때 항상 Bean이 재생성된다. (destroy -> construct)<br/>

- test
http://localhost:8888/{yml-file-name}/{profile}/default




```sh
curl http://localhost:8888/ecommerce/dev
```

[참조]<br/>
https://docs.spring.io/spring-cloud-config/docs/current/reference/html/<br/>
https://coe.gitbook.io/guide/config/springcloudconfig<br/>
https://soshace.com/spring-cloud-config-refresh-strategies/<br/>