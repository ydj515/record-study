# Spring
![111](https://user-images.githubusercontent.com/32935365/62720125-4fbf7280-ba44-11e9-9c40-de7974831d59.PNG)  
-https://github.com/ydj515/WebFrameWork2_Report1  
-https://github.com/ydj515/WebFrameWork2_Report2

## What is Spring
- Java/JSP 기반의 웹 프레임워크
- Java Virtual Machine 위에서 돌아가며, 아파치 라이선스 2.0을 따르는 오픈 소스 프레임워크
- 한국 전자정부표준프레임워크의 기반 기술이며 한국정보화진흥원에서는 공공기관의 웹 서비스 제공 시 스프링을 권장하고 있다.

## Feature of Spring
- **POJO**(Plain Old Java Object) 방식  
-특정 인터페이스를 **직접 구현하거나 상속받을 필요가 없어** 기존 라이브러리를 지원하기가 용이하고, 객체가 가볍다.

- **AOP**(Aspect Oriented Programming, 관점 지향 프로그래밍)  
-로깅, 트랜잭션, 보안 등 여러 모듈에서 **공통적으로 사용하는 기능을 분리하여 관리**  
-**AspectJ**를 포함하여 사용할 수 있고, 스프링에서 지원하는 실행에 조합하는 방식도 지원한다.  
-https://github.com/ydj515/helloAOP

- **DI**(Dependency Injection)  
-프로그래밍에서 구성요소 간의 의존 관계가 소스코드 내부가 아닌 **외부의 설정파일을 통해 정의**되는 방식  
-코드 재사용을 높여 소스코드를 다양한 곳에 사용할 수 있으며 **모듈간의 결합도도 낮춤**  
-계층, 서비스 간에 의존성이 존재하는 경우 스프링 프레임워크가 **서로 연결**시켜준다.  
-https://github.com/ydj515/helloDI
- **IoC**(Inversion of Control, 제어 반전)  
-외부 라이브러리 코드가 개발자의 코드를 호출하게 됨
-제어권이 프레임워크에게 있어 필요에 따라 **스프링 프레임워크가 사용자의 코드를 호출**

- **Life Cycle**(생명주기)  
-**스프링 프레임워크는 Java 객체의 생성, 소멸을 직접 관리**하며 필요한 객체만 사용할 수 있음
-myBatis와 같은 데이터베이스 처리 라이브러리나 tiles 같은 유용한 인터페이스를 제공

## Structure of Spring
![222](https://user-images.githubusercontent.com/32935365/62720826-d032a300-ba45-11e9-991d-f1f7bd84b91c.PNG)  
- Core : 제어 반전(IoC)과 의존성 주입(DI) 기능을 제공
- DAO : JDBC 추상 계층을 제공
- ORM : JPA, MyBatis, Hibernate와 같은 ORM API들과 통합할 수 있는 기능을 제공
- AOP : 스프링 프레임워크에서 제공하는 AOP 패키지를 제공
- Web : Spring Web MVC, Struts, WebWork 등 웹 어플리케이션 구현에 도움되는 기능을 제공

## Spring MVC Framework
- **Model** : POJO
- **View** : HTML output
- **Controller** : 모델을 다루고 적절한 View를 rendering 해줌  
![1](https://user-images.githubusercontent.com/32935365/62798081-5c14ff80-bb18-11e9-832e-3fed980b3fcd.PNG)

- **Dispatcher servlet**  
  -front controller의 역활로써 "/"이하의 모든 request를 처음 받는 주체
- **Handler Mapping**  
  -request URL과 controller class를 XML 설정과 annotation을 보고 mapping 시켜줌
- **Controller**  
  -request를 받아서 다른 business/service class를 호출하며 model object를 view로 보내줌
- **View Resolver**  
  -view의 logical name을 토대로 physical view file을 찾음
- **View**  
  -physical view file

## Required Configuration
- **Maven Configuration**  
  -pom.xml
- **Web deployment descriptor**  
  -web.xml
- **Spring MVC Configuration**  
  -root-context.xml  
  -servlet-context.xml  
  
### Maven Configuration  
- **pom.xml**
```xml
 <!-- application 식별자 역활-->
<groupId>kr.ac.hansung</groupId>
<artifactId>helloSpringMVC</artifactId>
<name>helloSpringMVC</name>
<packaging>war</packaging>
<version>1.0.0-BUILD-SNAPSHOT</version>
```

```xml
<!-- Spring -->
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-context</artifactId>
  <version>${org.springframework-version}</version>
  <exclusions>
    <!-- Exclude Commons Logging in favor of SLF4j -->
    <exclusion>
      <groupId>commons-logging</groupId>
      <artifactId>commons-logging</artifactId>
    </exclusion>
  </exclusions>
</dependency>
```

```xml
<!-- Spring MVC -->
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-webmvc</artifactId>
  <version>${org.springframework-version}</version>
</dependency>
```

```xml
<!-- spring jdbc -->
<dependency>
  <groupId>org.springframework</groupId>
  <artifactId>spring-jdbc</artifactId>
  <version>${org.springframework-version}</version>
</dependency>

<!-- commons-dbcp2 -->
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-dbcp2</artifactId>
  <version>2.1.1</version>
</dependency>

<!-- mysql-connector-java -->
<dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>8.0.11</version>
</dependency>
```

### Web deployment descriptor
- **web.xml**

```xml
<!-- 공유되는 bean... contextloadlistener가 읽어서 container를 구성 -->
<context-param>
  <param-name>contextConfigLocation</param-name>
  <param-value> <!-- 각 xml 설정파일을 등록해야지만 사용 가능-->
  /WEB-INF/spring/appServlet/dao-context.xml
  /WEB-INF/spring/appServlet/service-context.xml
  /WEB-INF/spring/appServlet/security-context.xml
  </param-value>
</context-param>

<listener>
  <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>

<servlet>
  <servlet-name>appServlet</servlet-name>
  <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class> <!-- 1. DispatcherServlet 동작-->
  <init-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value> <!-- 2. servlet-context.xml이라는 설정파일 읽음-->
  </init-param>
  <load-on-startup>1</load-on-startup>
</servlet>

<servlet-mapping>
  <servlet-name>appServlet</servlet-name>
  <url-pattern>/</url-pattern>
</servlet-mapping>
```

### **Spring MVC Configuration**
- **root-context.xml**
- **servlet-context.xml**
-Dispatcher Servlet이 읽어들이는 설정파일
```xml
<!-- DispatcherServlet Context: defines this servlet's request-processing infrastructure -->

<!-- annotation 기능 활성화 -->
<annotation-driven />

<!-- Handles HTTP GET requests for /resources/** by efficiently serving up static resources in the ${webappRoot}/resources directory -->
<resources mapping="/resources/**" location="/resources/" /> <!-- 정적인page정의 어차피 controller가 관여안하니깐 중요하지않다 -->

<!-- Resolves views selected for rendering by @Controllers to .jsp resources in the /WEB-INF/views directory -->
<!-- View Resolver-->
<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
  <beans:property name="prefix" value="/WEB-INF/views/" />
  <beans:property name="suffix" value=".jsp" />
</beans:bean>

<!-- 패키지를 scan 해서 controller, component와 같은 것을 자동으로 bean으로 등록해줌-->
<context:component-scan base-package="kr.ac.hansung.controller" />
```


[이미지 출처]  
https://namu.wiki/w/Spring(%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)  
