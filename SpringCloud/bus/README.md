# SpringCloud - bus
![bus](https://github.com/ydj515/record-study/assets/32935365/7b3618c9-554c-4a82-a1c3-833cb834ec38)

config가 변경 되면 마이크로 서비스들은 최신값을 가져오기 위해 `{microservice host}/actuator/refresh`를 호출해야하기에 번거로움에 따라 AMQP를 사용하여 broadcast하는 방식<br/>
spring cloud config server를 먼저 작업하고 아래의 내용을 추가<br/>
코드 저장소(github, gitlab, bitbucket 등)에 webhook 기능을 사용하여 설정파일 변경이후에 commit, push가 일어날 때마다 자동으로 모든 클라우드 노드의 refrshscope 가 적용된 어플리케이션이 환경설정을 다시 읽게 할 수 있음<br/>

- gradle
```gradle
  implementation 'org.springframework.boot:spring-boot-starter-actuator'
  implementation 'org.springframework.cloud:spring-cloud-starter-config'
  implementation 'org.springframework.cloud:spring-cloud-starter-bus-amqp'
```

- application.yml
```yml
spring:
  rabbitmq:
    host: localhost
    port: 5672
    username: guest
    password: guest

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

- rabbitmq start
docker로 rabbitmq 실행 후 `http://localhost:15672/` 접속 후 id, pw는 둘 다 guest 입력 후 서비스 확인
```sh
docker run -d --hostname rabbit --name rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3.7.5-management
```

- test
```sh
curl -X POST http://localhost:8000/actuator/bus-refresh
```


[참조]<br/>
https://docs.spring.io/spring-cloud-bus/docs/4.0.3/reference/html/<br/>
https://free-strings.blogspot.com/2016/01/spring-cloud-config.html<br/>
