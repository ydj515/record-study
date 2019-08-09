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
  -POM.xml
- **Web deployment descriptor**  
  -web.xml
- **Spring MVC Configuration
  -root-context.xml
  -servlet-context.xml

[이미지 출처]  
https://namu.wiki/w/Spring(%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)  
