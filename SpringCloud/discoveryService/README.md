# SpringCloud - discovery service

## discovery service
IP와 Port정보가 Auto-scaling 등으로 인해 동적으로 바뀌게 되는 클라우드 환경에서 특정 서비스를 식별할 수 있음.<br/>
Service Discovery는 서비스의 위치와 가용 상태 등을 관리하여 클라이언트 서비스가 요청할 서비스를 식별 가능하게 함.<br/>

- `Client Side Discovery`
생성된 서비스는 Service Registry에 서비스를 등록되고, 서비스를 사용할 클라이언트는 Service Registry에서 서비스의 위치를 찾아 호출하는 방식<br/>
![client-side](https://github.com/ydj515/record-study/assets/32935365/82649696-b4ed-44ee-b73e-65284165efce)


- `Server Side Discovery`
서비스를 사용할 클라이언트와 Service Registry 사이에 Load Balancer를 두는 방식<br/>
클라이언트는 Load Balancer에 서비스를 요청하고 Load Balancer가 Service Registry에 호출할 서비스의 위치를 질의하는 방식<br/>
eurka server가 faile over 및 load balnacer를 담당.<br/>
![server-side](https://github.com/ydj515/record-study/assets/32935365/b1b791e4-ad83-4da9-b534-4cc46adefac1)


#### Eureka
라우드 환경의 다수의 서비스(예: API 서버)들의 로드 밸런싱 및 장애 조치 목적을 가진 미들웨어서버.<br/>
rest 기반으로 작동하며 각 client의 ip, port, instnace id를 가지고 있다.<br/>
서비스가 Eureka Server에 등록될 때 자신이 살아있다는 상태값을 보낸다.<br/>
그리고 Eureka Server는 다른 Eureka Client의 정보들을 제공하고 서비스는 Local Cache에 저장<br/>
이후 30초(Default)마다 Eureka Server에 Heartbeats 요청을 보내고 Eureka Server는 90초 안에 Headerbeats가 도착하지 않으면 해당 Eureka Client를 제거<br/>
<strong>discovery service로 eureka를 사용한다.</strong><br/>

![eureka](https://github.com/ydj515/record-study/assets/32935365/5f5ad08c-1055-4ff9-9160-1349631cbbf6)


#### Eureak API
- `POST /eureka/apps/appID` : Eureka Client 등록
- `DELETE /eureka/apps/appID/instanceID` : Eureka Client 삭제
- `PUT /eureka/apps/appID/instanceID` : Heartbeats
- `GET /eureka/apps` : Eureka Client 목록


#### Eureka master server
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
    fetch-registry: false  #eureka server를 registry에 등록할지 여부
    register-with-eureka: false #registry에 있는 정보들을 가져올지 여부
```

#### Eureka master client
- main
```java
@SpringBootApplication
@EnableDiscoveryClient
public class UserServiceApplication {

    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }

}
```

- gradle
```gradle
	implementation 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-client'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
```

- application.yml
```yml
server:
  port: 9001

spring:
  application:
    name: user-service

eureka:
  instance:
    instance-id: ${spring.cloud.client.hostname}:${spring.application.instance_id:${random.value}}
  client:
    register-with-eureka: true
    fetch-registry: true
    service-url:
      defaultZone: http://localhost:8761/eureka #Eureka Server
```
[참조]<br/>
https://github.com/Netflix/eureka/wiki/Eureka-at-a-glance