# Spring
![111](https://user-images.githubusercontent.com/32935365/62720125-4fbf7280-ba44-11e9-9c40-de7974831d59.PNG)  
-https://github.com/ydj515/WebFrameWork2_Report1  
-https://github.com/ydj515/WebFrameWork2_Report2  
-https://github.com/ydj515/helloSpringMVC

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
-https://github.com/ydj515/helloSpringMVC
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

### Required Configuration
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

## Spring Security
-https://github.com/ydj515/helloSpringMVC
- Use Case
- Authentication(인증)
- Authorization(권한)
- CSRF
- Filter(DelegatingFilterProxy)

### Use Case
![11](https://user-images.githubusercontent.com/32935365/62962415-da83e100-be39-11e9-9bcf-b4aa1485291d.PNG)  

### Authentication
-자신이 누구라고 주장하는 사람을 확인하는 절차  
ex) admin, user ...

### Authorization
-가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻도록 허용하는 과정  
ex) id, password

### CSRF
**CSRF(Cross site request forgery, 사이트간 요청 위조)** 란 웹 사이트의 취약점을 이용하여 사용자가 의도하지 않는 요청을 송신하도록 하는 공격의 의미합니다. 이는 http프로토콜의 상태없음(stateless) 특성에 기인한 특정 웹 어플리케이션에 대한 일련의 요청들의 상관관계를 특정할 수 없기 때문에 세션 유지등에 일반적으로 사용되는 쿠키 정보 등이 조건만 만족한다면 자동적으로 송신되기 때문에 가능합니다. 여기서 상관관계를 특정할 수 없다는 의미는 예를 들어 카트화면 -> 주문정보 입력 -> 주문완료로 이어지는 주문 프로세스를 가진 웹 어플리케이션에서 각각의 페이지에대한 요청이 연속적으로 이어지는지에 대한 제어를 할 수 없다는 것을 의미합니다. 이 공격수법은 결과적으로 피해자가 의도한 요청과 동일한 과정으로 진행되므로 공격자에 대한 추적이 어려울 수 있으며 피해자에게 인가된 범위안에서만 공격이 이루어진다는 특징이 있습니다.(피해자가 특정 웹 어플리케이션의 관리자 계정으로 인증&인가된 상태라면 피해범위가 커질 수 있습니다.)

#### 대략적인 공격 시나리오
공격자가 공격코드를 가진 웹페이지를 제작하여 공개하거나 특정 웹 사이트에 공격용 코드를 삽입
피해자가 공격자가 준비해둔 페이지에 접속
피해자(피해자의 브라우저)는 공격자가 준비해둔 요청을 서버로 송신

#### 공격방법
-CSRF공격방법에는 정형화된 수법이 있다기 보다는 웹에 요청을 보낼수 있는 모든 방법이 공격방법이 된다고 할 수 있다. javascript와 ajax를 이용한 방법, **전통적인 form방법**, img태그를 이용한 방법 등등 요청을 보낼수 있는 방법이라면 그 어떤 것이라도 가능하다.

#### 대책
일반적으로 가장 널리 이용되는 방법에는 Synchronizer token pattern(동기화된 토큰 패턴)이 있다. 이 패턴은 서버 사이드(세션 스코프 등)에 보관된 토큰을 CSRF방어가 필요한 요청마다 포함(**요청할 form에 hidden필드를 이용하여 토큰을 추가**)시켜서 요청하고 서버에서 비교하는 방식으로 CSRF를 방어하는 방법이다. 가장 간단한 방식으로 사용자 경험에 영향을 주지 않는 방식으로 방어할 수 있으므로 널리 사용된다. 이 경우 토큰은 세션ID와 동일한 수준의 보호 수단이 필요하다.(SSL이용, URL노출 금지, 출력대상 페이지 캐시 컨트롤, xss취약점 방어 등등) 토큰의 유출이 염려스러운 경우 토큰 갱신 혹은 세션 파기 등등 즉각적인 조치가 필요하다.

#### pom.xml
```xml
<!-- spring-security-config -->
<dependency>
  <groupId>org.springframework.security</groupId>
  <artifactId>spring-security-config</artifactId>
  <version>${spring-security-version}</version>
</dependency>

<dependency>
  <groupId>org.springframework.security</groupId>
  <artifactId>spring-security-web</artifactId>
  <version>${spring-security-version}</version>
</dependency>

<dependency>
  <groupId>org.springframework.security</groupId>
  <artifactId>spring-security-core</artifactId>
  <version>${spring-security-version}</version>
</dependency>
```

#### loginFormExample.jsp
```jsp
<form name='f' action="<c:url value="/login"/>" method='POST'>
  <!-- error message 출력-->
  <c:if test="${not empty errorMsg }">
    <div style="color: #ff0000">
      <h3>${errorMsg }</h3>
    </div>
  </c:if>

  <table>
    <tr>
      <td>User:</td>
      <td><input type='text' name='username' value=''></td>
    </tr>

    <tr>
      <td>Password:</td>
      <td><input type='password' name='password' value=''></td>
    </tr>

    <tr>
      <td colspan='2'><input name="submit" type="submit" value="Login"></td>
      <td><input type='text' name='username' value=''></td>
    </tr>
  </table>
  
  <!-- csrf token -->
  <input type="hidden" name="${_csrf.parameterName}" value="${_csrf.token}" />

</form>
```

### Filter(DelegatingFilterProxy)

![1](https://user-images.githubusercontent.com/32935365/62962244-811bb200-be39-11e9-8033-457f6115e3eb.PNG)  

#### web.xml
```xml
<!-- 공유되는 bean... contextloadlistener가 읽어서 container를 구성 -->
<context-param>
  <param-name>contextConfigLocation</param-name>
  <param-value>
  /WEB-INF/spring/appServlet/dao-context.xml
  /WEB-INF/spring/appServlet/service-context.xml
  /WEB-INF/spring/appServlet/security-context.xml <!-- sercurity-context.xml이 security config xml file -->
  </param-value>
</context-param>
```

```xml
<filter>
  <filter-name>springSecurityFilterChain</filter-name>
  <filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class> <!-- spring에서 제공하는 filter 이름-->
</filter>

<filter-mapping>
  <filter-name>springSecurityFilterChain</filter-name>
  <url-pattern>/*</url-pattern>
</filter-mapping>
```

#### security-context.xml
```xml
<security:authentication-manager>
  <!-- 메모리 -->
  <!-- <security:authentication-provider>
    <security:user-service>
      <security:user name="nykim" authorities="ROLE_USER" password="letmein" />
    </security:user-service>
  </security:authentication-provider> -->

  <!-- DB에서 권한을 읽어 들인다. -->
  <security:authentication-provider>
    <security:jdbc-user-service data-source-ref="dataSource"
      users-by-username-query="select username, password, enabled from users where username=?"
      authorities-by-username-query="select username, authority from authorities where username=?" />
  </security:authentication-provider>
</security:authentication-manager>

<security:http auto-config="true" jaas-api-provision="true" use-expressions="true"> <!-- auto-config="true"라고 하면 spring이 로그인절차, 인증절차(DB에 있는지 없는지), 로그아웃 절차를 알아서 해줌-->
  <security:intercept-url pattern="/" access="permitAll" /> <!-- "/" 경로는 모두 접근 가능 -->
  <security:intercept-url pattern="/login" access="permitAll" /> <!-- "/login" 경로는 모두 접근 가능 -->
  <security:intercept-url pattern="/logout" access="permitAll" /> <!-- "/logout" 경로는 모두 접근 가능 -->
  <security:intercept-url pattern="/offers" access="permitAll" /> <!-- "/offers" 경로는 모두 접근 가능 -->
  <security:intercept-url pattern="/createoffer" access="isAuthenticated()" /> <!-- "/createoffer" 경로는 인증된 사용자만 접근 가능 -->
  <security:intercept-url pattern="/resources/**" access="permitAll" /> <!-- "/resources/**" 경로는 모두 접근 가능 -->

  <!-- 그외의 나머지 -->
  <security:intercept-url pattern="**" access="denyAll" />
  <security:form-login login-page="/login" /> <!-- security에서 제공하는 basic login form 대신해서 내가 custom한 login page를 -->
  <security:logout /> <!-- security에서 제공하는 basic logout form -->
</security:http>
```

## Logging with SLF4J & Logback
- 코드는 밑에 있엉
-https://github.com/ydj515/helloSpringMVC/blob/master/src/main/java/kr/ac/hansung/controller/HomeController.java
- debugging과 recording user interation  

사진



### Logging vs. debugger
- logging은 사용자 개입이 필요 x -> 오로지 기록만
- debugger는 사용자의 개입이 필요 o -> ex) break

### Logging Configuration
#### pom.xml

```xml
<!-- Logging -->
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-api</artifactId>
  <version>${org.slf4j-version}</version>
</dependency>
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>jcl-over-slf4j</artifactId>
  <version>${org.slf4j-version}</version>
  <scope>runtime</scope>
</dependency>

<dependency>
  <groupId>ch.qos.logback</groupId>
  <artifactId>logback-classic</artifactId>
  <version>1.2.3</version>
  <scope>compile</scope>
</dependency>
```


## Spring Web Form
- https://github.com/ydj515/helloSpringMVC

### sf 활성화
-JSP 상단에 넣어야함
```jsp
<%@ taglib prefix="sf" uri="http://www.springframework.org/tags/form"%>
```
- form
```jsp
<sf:form method="post" action="${pageContext.request.contextPath}/docreate"	modelAttribute="offer">
  <!-- offer라는 객체에 path값을 매칭 -->
  <table class="formtable">
    <tr><td class="label">Name:</td><td><sf:input class="control" type="text" path="name" /> <br/>
    <tr><td class="label">Email :</td><td><sf:input class="control" type="text" path="email" /><br/>
      <sf:errors path="email" class="error" /></td></tr>
    <tr><td class="label">Offer :</td>	<td><sf:textarea class="control" path="text" rows="10" cols="10"/><br/>
      <sf:errors path="text" class="error" /></td></tr>
    <tr><td class="label"></td>	<td><input class="control" type="submit" value="새 제안" /></td></tr>
  </table>
</sf:form>
```
- 다음 페이지 에선 이렇게 볼 수 있다
```jsp
${offer.name}가 새로운 제안을 하였습니다. 감사합니다.<br/>
```


[이미지 출처]  
https://namu.wiki/w/Spring(%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)  
https://postitforhooney.tistory.com/entry/SpringCSRF-CSRF란-무엇인가
