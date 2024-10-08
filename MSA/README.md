# MSA

## MSA & Monolithic & SOA

#### Monolithic Architecture

- 싱글모듈

  > 모든 소스가 단일 모듈 내에 존재
  > 응집성과 결합도 높음
  > 최상위 싱글 패키지
  > 유연성, 확장성이 제한적
  > 간단하게 1개의 jar

- 멀티모듈 아키텍처

  > 역할, 서비스 별로 모듈화
  > 응집성과 결합도 낮음
  > 최상위 멀티 패키지
  > 유연성, 확장성이 비교적 좋음
  > 간단하게 n개의 jar

- 장점

  > 배포가 간단
  > 비싼 서버 리소스를 최적화해서 사용이 가능
  > 공통 모듈을 활용하기 쉬움

- 단점
  > scale out이 어려움. (단일 db endpoint를 가지고 있어 의존성이 큼)
  > 단순한 수정사항일 지라도 전체 어플리케이션 재기동 필요
  > 장애시 전체 어플리케이션 영향을 받음

#### SOA

Service Oriented Architecture <br/>
Monolithic Architecture의 단점을 해결하고자 고안

> "서비스" 단위로 개발하고, 서비스 간 규격화된 프로토콜(인터페이스) 를 사용하여 통신
> 대개 동일한 기술 스택들을 가지고 서비스들을 개발하며, 각 서비스들간의 재사용이 목적.
> ESB(Enterprise Service Bus) 라는 개념을 통해, 요청에대해 어떤 서비스들을 호출할 지 캡슐화 된 Layer 존재
> 서비스 간 통합을 강조

#### SOA와 모놀리식 공통점

> shared db
> 모듈/서비스 간 규격화된 호출 방식 사용 (서비스 간 통합 관점)

#### SOA와 모놀리식 차이점

> soa는 독립적 배포 가능
> 트랜잭션 구현은 별개로 해야함
> 비즈니스 로직에 따라, 어떤 서비스를 호출할 지 결정하는 Layer 존재
> ESB의 관리

#### SOA 와 MSA 공통점

> 개발의 단위를 <b>서비스</b>로 인지
> 다른 서비스와 독립적으로 개발, 배포 가능
> SOA 에서는 ESB의 역활이 중요. MSA에서는 이러한 것이 단지 dumb pipe 의 기능만 작용하길 희망(중요 역활이 아닌 전달 그 자체로만의 역활만 수행)

#### SOA 와 MSA 차이점

> msa는 각 서비스는 각 서비스의 특성에 맞는 기술스택을 독립적으로 선택 가능

#### MSA

business capabilities를 확보하기 고안 <br/>
비즈니스에 따라 빠른 출시와 지속적 피드백을 가능하게 하는 설계 및 개발
아래의 기술들을 사용

- 감지(circuit breaker)
  > a -> b -> c 로 갈때 b -> c로 가는 통로의 장애가 발생한다면 b -> c로 가는 통로를 막고 b -> c' 로 진행하게함. 또한 b -> c 로가는 통로의 복구가 된다면 다시 b -> c로 진행
- 복구(container ochestration, K8S)

  > 복구. 컨테이너 등을 다루는 기술

- 의도치 않은 결과 방지(transaction, event driven)

  > a -> b -> c 로 흘러갈 때 b->c 구간에 에러가 발생하면 b는 작업이 완료되었음을 return 받지 못함. 하나의 event 자체를 a, b, c 가 구독하는 상태이고 b에서 완료된 작업을 c가 구독하여 처리한다고 가정하였을 때 b->c 의 작업요청은 실패했을 지라도 c 자체의 작업은 성공하였다.(message broker가 고장나지않았다면. )
  > saga(보상 트랜잭션)

- 서비스간의 영향도(chaos test)
  > 강제로 문제를 만들어보고 미리 실패해보고 테스트를 진행 ex) 복구하는 방법 등
  > 미리 실패하는 테스트를 진행해보면 실패하는 루트를 찾아 미리 방지

![111](https://github.com/ydj515/record-study/assets/32935365/a543df58-78bd-492a-9098-642de33e6812)

## MSA 패턴들

#### 통신 패턴

MSA 설계를 통해 도출된 서비스 간 어떤 방식으로 통신을 할 지 결정하는 패턴

- <strong>sync pattern</strong>
  어떤 서비스가 다른 서비스로 특정 Request 이후, 그 Response 를 받을 때까지 멈춰있어도 되는 경우<br/>
  ex) HTTP(Restful), gRPC

- <strong>async pattern</strong>
  어떤 서비스가 다른 서비스로 특정 Request 이후, 그 Response 를 당장은 받지 않아도 되는 경우<br/>
  ex) Kafka 등을 이용한 Message Queueing, Callback, Polling

#### 트랜잭션 패턴

MSA 설계를 통해 도출된 서비스를 사용하여 트랜잭션을 해결해 주기 위한 패턴

- <strong>2PC(2Phase Commit)</strong>
  2PC은 두 단계로 구분되어 작동함.<br/>

<strong>Prepare Phase (준비 단계)</strong>: 트랜잭션 매니저 (TM)는 모든 리소스 매니저 (RM)에게 트랜잭션 커밋 준비를 알림. RM들은 이 요청을 받고 필요한 모든 작업을 준비하며 준비가 완료되면 응답. <br/>

<strong>Commit/Rollback Phase (커밋/롤백 단계)</strong>: 모든 RM이 준비되면 TM은 트랜잭션을 커밋. 만약 어떤 RM이 준비되지 않았다면, TM은 트랜잭션을 롤백<br/>

- <strong>Compensating Transactions (보상 트랜잭션)</strong>
  보상 트랜잭션은 분산된 트랜잭션 중 일부가 실패할 경우, 그 실패 전에 성공적으로 완료된 트랜잭션을 보상 즉, 되돌리는 역할을 하는 트랜잭션<br/>
  SAGA 패턴의 트랜잭션은 분산된 여러 독립적인 트랜잭션이기 떄문에, 어떤 서비스의 트랜잭션이 실패하면 단일 트랜잭션 처럼 롤백 메커니즘을 사용할 수 없습니다. 대신 보상 트랜잭션을 사용하여 이전에 성공한 트랜잭션의 효과를 취소<br/>
  보상트랜잭션도 하나의 트랜잭션이기 때문에, 다양한 요인들로 인해 실패할 수 있음<br/>

- <strong>Saga Pattern (사가 패턴)</strong>
  SAGA 패턴은 MSA환경에서 일관성을 지키기 여렵다는 것을 기반으로, 약간의 일관성을 포기하고 Eventual Consistency(최종 일관성)을 보장하여 효율성을 높이기 위한 패턴

2PC에서는 트랜잭션을 하나의 트랜잭션으로 묶어서 처리를 하지만, SAGA 패턴은 긴 트랜잭션을 여러 개의 짧은 로컬 트랜잭션으로 분리하는 접근 방식.<br/>
각 트랜잭션은 다른 트랜잭션의 완료를 기다리지 않고 독립적으로 실행되기 때문에 트랜잭션의 원자성을 지켜줄 방법이 필요<br/>
만약 중간에 문제가 발생하면, 보상(Compenstation) 트랜잭션이 실행되어 이전 트랜잭션을 롤백하는 것과 같은 효과를 가져옴<br/>
각 로컬 트랜잭션은 자신의 트랜잭션을 끝내고 다음 트랜잭션을 호출하는 메시지, 이벤트를 생성<br/>
사가 패턴은 이벤트기반으로 작동<br/>
보상 트랜잭션을 카프카 같은 데이터 스트리밍 서비스 같은곳에서 처리하게 하고 멱등키와 함께 재시도 프로세스를 추가<br/>
이후 N번이상 실패 할경우에는 어쩔수 없지만... 개발자가 수동으로 오류를 해결할 수 있게 알람을 주어야함<br/>

#### 데이터 쿼리 패턴

MSA 소프트웨어 아키텍처를 설계하면서 생긴 데이터 쿼리를 해결하기 위한 패턴

- <strong>API Aggregation 패턴</strong>
  클라이언트는 여러개의 end point로 요청을 보내지 않고 하나의 api로 제곹하는 패턴.<br/>
  클라이언트는 단일한 API 엔드포인트에 요청을 보내고, 이 요청은 여러 개의 마이크로서비스로 라우팅됨으로써 클라이언트는 필요한 데이터를 한곳으로 통합적으로 가져올 수 있음<br/>

- <strong>CQRS 패턴</strong>
  Command(Write, Update, Delete) 작업과, Query(Read) 작업의 Endpoint 를 분리하고
  Command 에서 발생된 데이터의 변경을 이벤트 발행을 통해 원하는 포맷대로 Query 를 위한 전용 데이터 구조를 만들어 복잡한 Query를 담당<br/>
  이벤트 소싱 패턴과 CQRS를 같이 사용할 때는, 이벤트 저장소가 쓰기 모델이 되며, 이것이 메인 저장소가 된다. 읽기 모델은 일반적으로 매우 역정규화된 materialized view를 제공

      - 명령(Command)은 데이터 중심적이 아니라 수행할 작업 중심이 되어야 한다. 예를 들면 '호텔룸의 상태를 예약됨으로 변경한다'가 아니라 '호텔 룸 예약'과 같이 생성 <br/>
      - 명령(Command)은 보통 동기적으로 처리되기보단, 비동기적으로 큐에 쌓인 후 수행 <br/>
      - 쿼리(Query)는 데이터 베이스를 결코 수정x. 쿼리(Query)는 어떠한 도메인 로직도 캡슐화하지 않은 DTO만을 반환
      - DB 업데이트와 이벤트 발행은 반드시 하나의 트랜잭션 안에서 이뤄져야함.

- <string>CQRS의 장점</string>
  - 독립적인 스케일링 : CQRS는 읽기와 쓰기 각각에 대해 독립적으로 스케일링을 하는 것을 가능하게 해준다. 이는 훨씬 더 적은 Lock 경합이 발생하는 것을 가능하게 한다.
  - 최적화된 데이터 스키마 : 읽기 저장소는 쿼리에 최적화된 스키마를 사용할 수 있고, 쓰기 저장소는 쓰기에 최적화된 스키마를 사용할 수 있다.
  - 보안 : 읽기와 쓰기를 분리함으로써 보안 관리가 용이해진다.
  - 관심사 분리 : 읽기와 쓰기에 대한 관심사 분리는, 시스템의 유지 보수를 더 쉽게 해 주고 유연하게 해 준다. 대부분의 복잡한 비즈니스 로직은 쓰기 모델에 들어가고, 상대적으로 읽기 모델은 간단해진다.
  - 간단한 쿼리 : 읽기 저장소의 materialized view를 통해, 복잡한 조인문을 사용하지 않을 수 있다.

https://www.baeldung.com/cqrs-event-sourcing-java

#### 테스트 패턴

분리된 서비스들이 서로 빈번하게 호출되는 모놀리식과는 다른 환경 MSA 환경에서, 여러 테스트 방식을 적용하여 테스트<br/>
ex) 단위 테스트, 통합 테스트, E2E 테스트(end to end)

#### 외부 API 패턴

서비스 간의 통신 시 구현과 관련된 종속성을 해결하기 위한 패턴.<br/>
어떤 서비스가 다른 특정 서비스를 호출할 때, 직접 호출하는 것이 아닌 리버스 프록시 역할을 하는 인터페이스
서비스를 제공하여 마이크로서비스 간 내부 구현방식과 무관하게 유연성을 가질 수 있는 패턴<br/>
=> 서비스 호출 시에는 <strong>필요한 데이터만</strong>, 실제 구현은 상황에 따라 유연하게.

#### 디스커버리 패턴

수 많은 컨테이너, 서버들의 상태를 정상적으로 관리하기 어려웠던 문제를 해결하기 위한 패턴.<br/>
수 많은 서비스들이 정상적으로 동작하는지를 판단하고, 상황에 따라 적절한 동작을 하는 메커니즘을 제공하는 패턴<br/>
ex) 쿠버네티스의 redisness probe, liveness probe

#### 가시성 패턴(observability)

구체적으로 어떻게 로깅, 메트릭을 저장하고 인덱싱하여 검색할 지에 집중하는 패턴<br/>
로깅, 모니터링의 어려움을 해결하기 위한 패턴<br/>
로깅 및 메트릭의 중앙집중 및 필터링 등을 통한 한곳에서의 모니터링<br/>
하나의 트랜잭션에 대해 각 서비스 요청들을 하나의 요청처럼 볼 수 있게하는 트레이싱<br/>

#### 신뢰성 패턴(reliability)

MSA 아키텍쳐를 설계하면서, 분리/분해로 인해 떨어진 신뢰성을 해결하기 위한 패턴. <br/>
**장애 복구, 자가 치유, 무정지 배포** 등을 구현하기 위한 패턴<br/>
신뢰성을 높히기 위한 패턴으로 분산시스템에서의 장애전파를 막고 피해를 최소화하기위한 패턴<br/>
ex) circuit breaker<br/>


## hexagonal architecture
각 계층에서 하던 일들을 "내부와 외부" 라는 개념으로 나누어 각각에 맞는 별도의 인터페이스를 정의<br/>
**adaptor**를 통해 외부 서비스의 의존성을 분리하여 언제든 쉽게 교체하여 유연한 확장성 있는 대처를 하고, **port**를 통해서 내부 비즈니스 로직과 인터페이스를 분리하여 내부 로직의 구현은 인터페이스와 무관하게 개발 가능<br/>

"내부"의 로직은 오직 "외부" 통해서만 접근이 가능<br/>
모든 외부 시스템과의 직접적인 상호작용은 "adaptor"의 역할<br/>
각 서비스에서 비즈니스 로직에 맞게 정의된 인터페이스는 "port"<br/>
즉, 외부 서비스와의 상호 작용(아답터) 는 비즈니스 로직과의 작업을 정의한 인터페이스(포트) 랑만 서로 통신<br/>

모든 비즈니스 로직은, 오직 외부에서 내부 방향 / 내부에서 외부 방향으로만 호출이 가능<br/>
- 인바운드 어댑터 -> 인바운드 포트 -> 비즈니스 로직
- 비즈니스 로직 -> 아웃바운드 포트 -> 아웃바운드 어댑터

<br/>

#### 어댑터 (Adapter)
서비스의 입장에서 이 서비스가 사용하는 외부 시스템과의 직접적인 구현 및 상호작용을 처리
- 외부 시스템(UI) 으로부터 들어온 Request 가 가장 처음 만나는 Controller 는 "인바운드 어댑터"
- 메세지 브로커(kafka) 로부터 Consume 하는 동작을 처리하는 로직 핸들러는 "인바운드 어댑터"
- DB(MySQL, ..) 에 직접적으로 접근하여 다양한 작업(CRUD) 을 처리하기 위한 DAO 는 "아웃바운드 어댑터"

#### 포트 (Port)
비즈니스 로직 입장에서 어댑터와 통신하기 위한 동작을 정의한 인터페이스
- Controller 로부터 들어온 요청으로부터 특정 비즈니스 로직을 수행하기 위한 동작을 정의한 인터페이스
- Consume 한 메세지를 처리하기 위한 비즈니스 로직의 동작을 정의한 인터페이스 -> "인바운드 포트"
- 비즈니스 로직에서 DB 접근을 위해서 정의한 Repository 인터페이스는 "아웃바운드 포트"


[출처]<br/>
https://rubygarage.org/blog/monolith-soa-microservices-serverless<br/>
https://mslim8803.tistory.com/73 <br/>
