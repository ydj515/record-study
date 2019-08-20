# SpringBoot
- https://github.com/ydj515/helloSpringBoot

## Spring Boot의 장점
- Spring의 설정을 복사 붙혀넣기 하는 번거로움 제거
- 자동으로 의존성 맞는 library 다운
- Embeded Tomcat으로 인해 Tomcat 따로 설치 필요 x
- 쉬운 설정

### Spring의 설정을 복사 붙혀넣기 하는 번거로움 제거
- web.xml의 Spring MVC dispatcher servlet 설정
```xml
<servlet>
  <servlet-name>appServlet</servlet-name>
  <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
  <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
  </init-param>
  <load-on-startup>1</load-on-startup>
</servlet>

<servlet-mapping>
   <servlet-name>appServlet</servlet-name>
  <url-pattern>/</url-pattern>
</servlet-mapping>
```

- Servlet-context.xml의 component scan, a view resolver, resources 설정
```xml
<!-- Enables the Spring MVC @Controller programming model -->
<annotation-driven />

<context:component-scan base-package="kr.ac.hansung.web.controllers" />

<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
 <beans:property name="prefix" value="/WEB-INF/views/" />
 <beans:property name="suffix" value=".jsp" />
</beans:bean>

<resources mapping="/resources/**" location="/resources/" />
```

- dao-context.xml의 datasource, A session factory, a transaction manager 설정
```xml
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource“  destroy-method="close">
 <property name="driverClassName" value="${jdbc.driverClassName}" />
 <property name="url" value="${jdbc.url}" />
 <property name="username" value="${jdbc.username}" />
 <property name="password" value="${jdbc.password}" />
</bean>

<bean id="sessionFactory“ class="org.springframework.orm.hibernate5.LocalSessionFactoryBean">
 <property name="dataSource" ref="dataSource"></property>
   …
 <property name="hibernateProperties">
     <props>
         <prop key="hibernate.dialect">org.hibernate.dialect.MySQLDialect</prop>
         <prop key="hibernate.hbm2ddl.auto">update</prop>
         <prop key="hibernate.show_sql">true</prop>
     </props>
  </property>
</bean>

<bean id=" txManager“ class="org.springframework.orm.hibernate5.HibernateTransactionManager">
  <property name="sessionFactory" ref="sessionFactory"></property>
</bean>
```
**위와 같은 설정을 여러번 반복 해서 해주어야 하는것을 해준다.**

### 자동으로 의존성 맞는 library 다운
- 밑의 pom.xml과 같이 설정만 해주면 web과 관련된 library를 자동으로 다운해준다  
```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-web</artifactId>
</dependency>
```



- **spring-boot-starter-web** - Web & RESTful applications  
- **spring-boot-starter-test** - Unit testing and Integration Testing  
- **spring-boot-starter-jdbc** - Traditional JDBC  
- **spring-boot-starter-security** - Authentication and Authorization  
- **spring-boot-starter-data-jpa** - Spring Data JPA with Hibernate  
- **Spring** : core, beans, context, aop
- **Web MVC** : (Spring MVC)
- **Jackson** : for JSON Binding
- **Validation** : Hibernate Validator, Validation API
- **Embedded Servlet Container** : Tomcat
- **Logging** : logback, slf4j



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
- @SpringBootApplication
    - @Configuration + @ComponentScan  + @EnableAutoConfiguration 
```java

```

## Example Code

### RequestMapping GET 대신 GetMapping
```java
@Controller
public class HomeController {

    // @RequestMapping(value=“/”, method = RequestMethod.GET).
    @GetMapping("/")
    public String home(Model model) {
	model.addAttribute("message", "hello world");
	return "index";
    }
}
```

### Form 태그에 CSRF 토큰 hidden x -> CSRF Security
```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
 
    @Override
    protected void configure(HttpSecurity http) throws Exception {
	http
	.authorizeRequests()
           .anyRequest()
            .permitAll()
            .and()
      .csrf().disable();
}
```
### JPA
```java
import org.springframework.data.repository.CrudRepository;

public interface CustomerRepository extends CrudRepository<Customer, Long> { // interface로 구현해서 자동적으로 알아서 class(CRUD) 만들어줌

	List<Customer> findByLastName(String lastName);

}
```
