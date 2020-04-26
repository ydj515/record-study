# DDD
- Domain Driven Design

## What is DDD
- 도메인 그 자체와 도메인 로직에 초점을 맞추는 디자인
- 일반적으로 많이 사용하는 데이터중심의 접근법을 탈피해서 순수한 도메인의 모델과 로직에 집중하는 것
- 보편적인 언어의 사용으로 도메인 전문가와 소프트웨어 개발자 간의 커뮤니케이션 문제를 없애고 상호가 이해할 수 있고 모든 문서와 코드에 이르기까지 동일한 표현과 단어로 구성된 단일화된 언어체계를 구축
- => 분석 작업과 설계 그리고 구현에 이르기까지 통일된 방식으로 커뮤니케이션이 가능해진다.
- 소프트웨어 엔티티와 도메인 컨셉트를 가능한 가장 가까이 일치시키는 것.
- 분석모델과 설계가 다르고 그것과 코드가 다른 구조가 아니라 도메인 모델부터 코드까지 항상 함께 움직이는 구조의 모델을 지향하는 것
- **DDD는 방법론이 아니고** 단지 도메인에 집중하라는 것

## Domain
- 소프트웨어가 취급하는 **어떤 활동이나 관심과 관계가 있는 지식**
- 소프트웨어가 해결해야되는 문제
- 소프트웨어가 복잡해지면 도메인의 복잡성도 증가
- 소프트웨어의 복잡성이 증가하면, 도메인의 복잡성이 증가
- 도메인은 어떤 소프트웨어의 기능이 아니라 소프트웨어 전체가 도메인이 될 수 있고 시스템 자체가 도메인이 될 수 있음
- ex) 온라인 서점에서 로그인을 해서 책을 비교 후 주문하는 전체 과정이 "ORDER"라는 전체과정으로 도메인이라고 할 수 있다.
- 즉, 도메인의 한 과정 안에 비지니스 로직이 포함된다는 말임.

## Domain Model
- 도메인을 분석하여 모델을 구분하는 일
- 도메인 모델링
- 도메인을 개념적으로 표현
- Setter는 지양하고, 객체 생성시에 모든 정보를 setting하게 유도.
- 아래는 Domain Model의 구성요소

### Entity
- 모델을 표현
- 고유 식별값을 가짐(UUID)
- 스스로의 라이프 사이클 소유

### Value
- 고유의 키값을 가지지 않음
- 데이터의 표현
- 속성의 불변성
- 실제 데이터는 String 형태가 많지만 단순히 문자열이 아니라 도메인에서 특별한 의미를 지니느 경우가 많기 때문에 식별자를  위한 벨류 타입을 사용해 의미가 잘 들어나도록 해야함
```java
public class Order {
    private int id;
    private int price;
    private String orderer;
    private int amounts;
    private String ordererPhonNum;

    ...

    public ing getId() {
        return id;
    }
    ...
}
```
위와 같은 주문 클래스는 아래와 같이 int, String 대신에 OrderNo value type만으로도 뚜렷하게 알 수 있게 한다.

```java
public class Order {
    private OrderNo id;
    private Money price;
    private Orderer orderer;
    private int amounts;

    ...
}

class orderer {
    private String nae;
    private String phoneNum;

    ...
}
```


### Aggregate
- 관련된 객체의 묶음
- 도메인 모델이 복잡할 수록 Aggregate의 관점에서 보아야함
- 개념상 완전한 한개의 도메인 모델을 표현하므로 객체의 영속성을 처리하는 Repository는 Aggregate의 단위로 존재
- EX) Order밑에 여러개의 Domain들이 있지만, 실제 DB(Repository)에는 하나만 영속화 함(여기선 극한의 예시임..)
- Aggregate와 Repository의 설계는 JPA, Hibernate.. MySql, MongoDB.. 등 어떤 기술을 사용하냐에 따라 다름
![1](https://user-images.githubusercontent.com/32935365/80296679-0b355c00-87b8-11ea-987c-4b68e246203f.jpg)  
- 아래와 같이 Aggregate를 나눈다.
![2](https://user-images.githubusercontent.com/32935365/80296694-1ab4a500-87b8-11ea-8510-03084113486e.jpg)  


### Repository
- Entity의 저장소
- Entity나 Value가 요구사항에서 도출되는 도메인 모델이라면 Repository는 **구현을 위한 도메인 모델**
- 어떤 기술을 사용해서 Repository를 구현하느냐에 따라 애그리거트의 구현도 영향을 받음

### Service
- Domain 객체에 위치시키기 어려운 오퍼레이션을 가지는 객체 
- Service Domain의 operation은 일반적으로 Stateless
- 여러 도메인을 다룰 수도 있음
