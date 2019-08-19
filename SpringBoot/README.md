# SpringBoot
- https://github.com/ydj515/helloSpringBoot

## Spring Boot의 장점
- Spring의 pom.xml을 복사 붙혀넣기 하는 번거로움 제거
- 자동으로 의존성 맞는 library 다운
- Embeded Tomcat으로 인해 Tomcat 따로 설치 필요 x


## Configuration

### Create Project
- Spring Boot -> Spring Starter Project
- 사용할 라이브러리 추가 ex) MVC ..

### application.properties
- src/main/resources/application.properties 설정

```properties
server.port=9000

spring.datasource.url=jdbc:mysql://localhost:3306/customerPortal
spring.datasource.username=root
spring.datasource.password=csedbadmin

spring.jpa.hibernate.ddl-auto=create

spring.mvc.viewprefix=/WEB-INF/jsp/
spring.mvc.viewsuffix=.jsp
```
### start Spring Boot
- src/main/java/HelloSpringBootApplication.java가 main
- Runs as - boot start

