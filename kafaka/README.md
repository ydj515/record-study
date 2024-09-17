# Kafaka

카프카(Kafka)는 파이프라인, 스트리밍 분석, 데이터 통합 및 미션 크리티컬 애플리케이션을 위해 설계된 고성능 분산 **이벤트 스트리밍 플랫폼**입니다.<br/>
이벤트 스트림을 **pub/sub** 구조를 통해 데이터를 지속적으로 가져오고 내보내며, 원하는 기간 동안 지속적으로 안정적으로 이벤트 스트림을 저장합니다.(**Pub-Sub 모델의 메세지 큐 형태로 동작**)<br/>

또한, 발생된 이벤트 스트림을 안정적으로 처리를 하는 기능을 가지고 있어 대용량 데이터 처리 및 실시간 데이터 스트리밍에 적합합니다.<br/>
확장성과 탄력성을 가지고있어 안전한 분산 방식을 제공하는 플랫폼으로 가상 머신, 컨테이너, 온프로미스, 클라우드 등 다양한 환경에서 배포를 할 수 있습니다.<br/>

## Kafka 주요 기능

- **분산 아키텍처** <br/>
  3개 이상의 n개의 브로커(카프카), 홀수개의 주키퍼로 구성된 클러스터로 데이터 및 처리 부하를 분산하여 확장성을 제공합니다.
- **내구성** <br/>
  디스크에 메세지가 저장되어 장애 시, 유실이 되지 않습니다.
- **고신뢰도 메세징** <br/>
  “적어도 한 번”, “많아도 한 번”, “정확히 한 번” 메세지 전달을 합니다.
- **실시간 데이터 처리** <br/>
  데이터 스트림을 Kafka API를 통해 처리하여 데이터 처리 엔진을 연결할 수 있습니다.
- **이벤트 브로커** <br/>
  메시지 브로커와 다르게 이벤트 브로커는 **이벤트 소싱 방식**이다. 이벤트 소싱이란 시스템에서 발생하는 **모든 이벤트를 기록하고 저장**하는 개념인데 카프카는 이러한 이벤트 소싱 아키텍처를 구현하는 데 사용된다. RabbitMQ 같은 메시지 브로커는 메시지가 사용 되면 사라지지만 이벤트 브로커는 메시지가 사라지지 않는다. 그렇기 때문에 서로 다른 애플리케이션에서 같은 이벤트를 각자 활용할 수 있다.

## Kafka 적용 모델

이전의 방식은 각 서버에서 각 애플리케이션에 통신하기에 각 모듈간 의존성이 높았다. 예를 들자면 A Server에서 ELK에 로그를 기록 시키려 했는데 ELK가 응답하지 않았을 때 데이터가 유실될 수 있다. 각각의 연결을 관리해야 하기 때문에 확장에 불리하다. 만약 새로운 Publisher 혹은 Subscriber가 생길 경우 복잡도가 증가한다. <br/>
<img width="516" alt="스크린샷 2024-09-17 오전 2 19 43" src="https://github.com/user-attachments/assets/f08b3f7b-60ff-474a-a3a9-b6c5a2e5b3e2">

아래의 그림처럼 앞서 설명한 기존 모델의 단점인 낮은 확장성, 높은 의존성을 해결하기위해 카프카를 활용한 Event Driven Architecture 에서는 그림 처럼 가운데 카프카가 들어가면서 구조가 상당히 단순해진다. Publisher는 메시지를 보내기만 하고 Consumer는 메시지를 받기만 한다. 중간에 누가 어떤 데이터를 받을지는 Broker인 카프카가 알아서 한다. 이러한 구조에서는 데이터를 받고싶은 Consumer, 데이터를 보내는 Publisher가 늘어나도 느슨한 결합의 상태를 유지할 수 있다. <br/>
<img width="516" alt="스크린샷 2024-09-17 오전 2 19 50" src="https://github.com/user-attachments/assets/244af9f9-0c2d-4b34-a173-d398b80716fb">

실제 적용 사례를 살펴보자. 아래는 기존의 링크드인의 데이터 처리 시스템이다. <br/>

<img width="742" alt="스크린샷 2024-09-17 오전 2 16 26" src="https://github.com/user-attachments/assets/a480607b-d312-40a6-a82a-8a400b6f7901">

각 애플리케이션과 DB가 end-to-end 로 연결되어 있고(각 파이프라인이 파편화 되어있음), 요구사항이 늘어남에 따라 데이터 시스템 복잡도가 높아지면서 다음과 같은 문제가 발생하게 되었다. <br/>

1. `시스템 복잡도 증가 (Complexity)` <br/>
   통합된 전송 영역이 없어 데이터 흐름을 파악하기 어렵고, 시스템 관리가 어려움<br/>
   특정 부분에서 장애 발생 시 연결 되어있는 애플리케이션들을 모두 확인해야 하기 때문에 조치 시간 증가<br/>
   HW 교체 / SW 업그레이드 시 관리포인트가 늘어나고, 작업시간 증가 (=> 연결된 애플리케이션에 side effect 가 없는지 확인해야 함)

2. `데이터 파이프라인 관리의 어려움` <br/>
   각 애플리케이션과 데이터 시스템 간의 별도의 파이프라인 존재하고, 파이프라인 마다 데이터 포맷과 처리 방식이 다름<br/>
   새로운 파이프라인 확장이 어려워지면서, 확장성 및 유연성이 떨어짐<br/>
   또한 데이터 불일치 가능성이 있어 신뢰도 감소<br/>

아래는 이러한 위의 실제 링크드 인의 데이터 처리 시스템에 kafka를 도입한 그림이다. <br/>

<img width="742" alt="스크린샷 2024-09-17 오전 2 16 32" src="https://github.com/user-attachments/assets/b53846a2-4a91-4816-ad35-44459adccd95">

kafka를 도입함으로써 모든 이벤트/데이터의 흐름을 중앙에서 관리할 수 있게 되었다.<br/>
새로운 서비스/시스템이 추가되도 카프카가 제공하는 표준 포맷으로 연결하면 되므로 확장성과 신뢰성이 증가하였다.<br/>
개발자는 각 서비스간의 연결이 아닌, 서비스들의 비즈니스 로직에 집중 가능해졌다.<br/>

## Kafka 구성 요소

- **Event** <br/>
  kafka에서 producer 와 consumer가 데이터를 주고받는 단위. 메세지

- **Producer** <br/>
  kafka에 이벤트를 게시(post, pop)하는 클라이언트 어플리케이션<br/>
  메시지를 만들어서 카프카 클러스터에 전송<br/>
  메시지 전송 시 Batch 처리가 가능<br/>
  key값을 지정하여 특정 파티션으로만 전송이 가능<br/>
  전송 acks값을 설정하여 효율성을 높일 수 있음<br/>
  ACKS=0 -> 매우 빠르게 전송. 파티션 리더가 받았는 지 알 수 없음<br/>
  ACKS=1 -> 파티션 리더가 받았는지 확인. 기본값<br/>
  ACKS=ALL -> 파티션 리더 뿐만 아니라 팔로워까지 메시지를 받았는 지 확인<br/>

- **Consumer** <br/>
  Topic을 구독하고 이로부터 얻어낸 이벤트를 받아(Sub) 처리하는 클라이언트 어플리케이션<br/>
  카프카 클러스터에서 메시지를 읽어서 처리<br/>
  메세지를 Batch 처리할 수 있음.<br/>
  한 개의 컨슈머는 여러 개의 토픽을 처리할 수 있음<br/>
  메시지를 소비하여도 메시지를 삭제하지는 않음(Kafka delete policy에 의해 삭제)<br/>
  한 번 저장된 메시지를 여러번 소비도 가능<br/>
  컨슈머는 컨슈머 그룹에 속함<br/>
  한 개 파티션은 같은 컨슈머그룹의 여러 개의 컨슈머에서 연결할 수 없음.(한개의 파티션은 컨슈머 그룹당 한개의 컨슈머.)<br/>

- **Topic** <br/>
  각각의 메시지를 목적에 맞게 구분할 때 사용(카테고리의 개념)<br/>
  메시지를 전송하거나 소비할 때 Topic을 반드시 입력<br/>
  Consumer는 자신이 담당하는 Topic의 메시지를 처리<br/>
  한 개의 토픽은 한 개 이상의 파티션으로 구성<br/>
  이벤트가 모이는 곳. producer는 topic에 이벤트를 게시하고, consumer는 topic을 구독해 이로부터 이벤트를 가져와 처리<br/>

- **Partition** <br/>
  분산 처리를 위해 사용<br/>
  Topic은 여러 Broker에 분산되어 저장<br/>
  Topic 생성 시 partition 개수를 지정할 수 있음.(파티션 개수 변경 가능. \*추가만 가능)
  파티션이 1개라면 모든 메시지에 대해 순서가 보장됨.<br/>
  파티션 내부에서 각 메시지는 offset(고유 번호)로 구분<br/>
  파티션이 여러개라면 Kafka 클러스터가 라운드 로빈 방식으로 분배해서 분산처리되기 때문에 순서 보장 X<br/>
  파티션이 많을 수록 처리량이 좋지만 장애 복구 시간 증가<br/>

- **Zoopeeper** <br/>
  분산 애플리케이션 관리를 위한 코디네이션 시스템<br/>
  분산 메시지큐의 메타 정보를 중앙에서 관리하는 역할<br/>
  Kafka의 메타데이터, 브로커 상태, 토픽, 컨트롤러등을 관리<br/>
  어떤 브로커가 특정 파티션 및 토픽의 리더인지 결정하고 리더 선택을 수행하는데 사용<br/>
  토픽 및 권한에 대한 구성을 저장<br/>
  새로운 토픽, 브로커 종료, 브로커 등장, topic 삭제 등 메타데이터와 관련있는 것들에 대해 변경사항이 있는 경우 Kafka에게 알려줌<br/>

### 하나의 topic을 여러개의 partition으로 분산시킨 이유

<img width="496" alt="스크린샷 2024-09-17 오전 2 03 39" src="https://github.com/user-attachments/assets/11e7e92f-6235-4098-91a2-2a5fe0e06827">

병렬로 처리하기 위해 하나의 topic을 여러개의 partition으로 분산 저장 한다.<br/>
카프카의 토픽에 메세지가 쓰여지는 것도 어느정도 시간이 소비된다. 몇 천건의 메세지가 동시에 카프카에 write 되면 병목현상이 발생할 수 있다.<br/>
따라서 파티션을 여러개 두어서 분산 저장함으로써 write 동작을 병렬로 처리할 수 있다.<br/>

다만, 한번 늘린 파티션은 절대 줄일 수 없기 때문에 운영 중에, 파티션을 늘려야 하는건 충분히 검토 후 실행되어야 한다. (최소한의 파티션으로 운영하고 사용량에 따라 늘리는 것을 권장한다)<br/>
파티션을 늘렸을 때 메세지는 Round-Robin 방식으로 쓰여진다. 따라서 하나의 파티션 내에서는 메세지 순서가 보장되지만, 파티션이 여러개일 경우에는 순서가 보장되지 않는다.<br/>

### consummer group

<img width="731" alt="스크린샷 2024-09-17 오전 3 48 26" src="https://github.com/user-attachments/assets/d5f37673-c925-45f9-a358-032c915e4e96">

consumer의 묶음을 consumer group이라고 한다.<br/>
컨슈머 그룹은 하나의 topic에 대한 책임을 갖고 있다.<br/>
즉 어떤 consumer가 down된다면, 파티션 재조정(리밸런싱)을 통해 다른 컨슈머가 해당 파티션의 sub을 맡아서 한다. offset 정보를 그룹간에 공유하고 있기 때문에 down 되기 전 마지막으로 읽었던 메세지 위치부터 시작한다.<br/>

## Kafka 특징

kafka의 특징및 장단점은 아래와 같다.

### 동작 원리

publisher는 전달하고자 하는 메세지를 topic을 통해 분류한다.<br/>
subscriber는 원하는 topic을 구독(=subscribe)함으로써 메시지를 읽는다.<br/>
publisher와 subscriber는 오로지 topic 정보만 알 뿐, 서로에 대해 알지 못할 뿐더라 알필요가 없다.<br/>
kafka는 broker들이 하나의 클러스터로 구성되어 동작하도록 설계되었다.<br/>
클러스터 내, broker에 대한 분산처리는 ZooKeeper가 담당한다.(현재는 kraft모드를 사용한다.)

### 장점

대규모 트래픽 처리 및 분산 처리에 효과적이다.<br/>
클러스터 구성, Fail-over, Replication 같은 기능이 있음<br/>
100Kb/sec 정도의 속도 (다른 메세지 큐 보다 빠름)<br/>
디스크에 메세지를 특정 보관 주기동안 저장하여 데이터의 영속성이 보장되고 유실 위험이 적다. 또한 Consumer 장애 시 재처리가 가능하다.<br/>

### 단점

카프카 클러스터를 운영하기 위해서는 컴퓨팅 자원을 많이 소모한다.<br/>
안정적으로 운영하기 위해서는 기본적으로 주키퍼와 카프카의 클러스터를 운영해야 하고 (카프카 4.0 버전 부터는 Kraft라는 방식으로 주키퍼 없이 운영이 가능) 속도 또한 RabbitMQ나 Redis Queue 보다는 느리다. 따라서 소규모 시스템에서는 RabbitMQ가 더 좋다.

## KRaft

<img width="579" alt="스크린샷 2024-09-17 오전 8 14 11" src="https://github.com/user-attachments/assets/f489756f-f2b7-4fd9-9737-4550748ceff3">

Apache Kafka의 새로운 협의 프로토콜이다.<br/>
Apache Kafka의새로운 메커니즘인 KRaft를 사용하면 메타데이터를 효율적으로 관리할 수 있다.<br/>
KRaft는 주키퍼의 의존성을 제거하고, 카프카 클러스터 내 컨트롤러가 선출된 후 메타데이터를 직접 관리한다. 이로 인해 성능과 안정성이 향상되며, 유지보수가 단순화되고, 병목현상이 줄어든다.

### zookeeper vs KRaft

이하 아래의 설명에서 zookeeper를 사용한 클러스터는 주키퍼 모드라고하고, KRaft를 사용한 클러스터는 KRaft 모드라고 한다.

#### zookeeper

<img width="601" alt="스크린샷 2024-09-16 오전 3 07 33" src="https://github.com/user-attachments/assets/23b9b504-4738-47fd-a29d-055fc28d0d24">

주키퍼 모드는 주키퍼 앙상블(Ensemble)과 카프카 클러스터가 존재하며, 카프카 클러스터 중 하나의 브로커가 컨트롤러 역할을 하게 됩니다.<br/>
컨트롤러는 파티션의 리더를 선출하는 역할을 하며, 리더 선출 정보를 브로커에게 전파하고 주키퍼에 리더 정보를 기록하는 역할을 합니다.<br/>
컨트롤러의 선출 작업은 주키퍼를 통해 이루어지는데, 주키퍼의 임시노드를 통해 이루어집니다.<br/>
임시노드에 가장 먼저 연결에 성공한 브로커가 컨트롤러가 되고, 다른 브로커들은 해당 임시노드에 이미 컨트롤러가 있다는 사실을 통해 카프카 클러스터 내 컨트롤러가 있다는 것을 인식하게 됩니다.<br/>
이를 통해 한 번에 하나의 컨트롤러만 클러스터에 있도록 보장할 수 있습니다.<br/>

#### KRaft

<img width="601" alt="스크린샷 2024-09-16 오전 3 07 46" src="https://github.com/user-attachments/assets/184a0c3e-07d9-4805-b677-9ffa6229e315">

KRaft 모드는 주키퍼와의 의존성을 제거하고, 카프카 단일 애플리케이션 내에서 메타데이터 관리 기능을 수행하는 독립적인 구조가 되는 것입니다.<br/>
주키퍼 모드에서 1개였던 컨트롤러가 3개로 늘어나고, 이들 중 하나의 컨트롤러가 액티브(그림에서 노란색 컨트롤러) 컨트롤러이면서 리더 역할을 담당합니다.<br/>
리더 역할을 하는 컨트롤러가 write 하는 역할도 하게 됩니다.<br/>
또한 주키퍼 노드에서는 메타 데이터 관리를 주키퍼가 했다면, 이제는 카프카 내부의 별도 토픽을 이용하여 메타 데이터를 관리합니다.<br/>
액티브인 컨트롤러가 장애 또는 종료되는 경우, 내부에서는 새로운 합의 알고리즘을 통해 새로운 리더를 선출하게 됩니다.<br/>
리더를 선출하는 과정을 간략히 설명드리자면, 후보자들은 적합한 리더를 투표하게 되고 후보자 중 충분한 표를 얻으면, 해당 컨트롤러가 새로운 리더가 됩니다.<br/>

### Controller Quorum 동작 방식

컨트롤러 노드가 외부 시스템에 의존하기 않게 Raft 합의 프로토콜을 사용하여 일관성과 Kafka의 리더 선택을 유지합니다.<br/>
활성 컨트롤러 (메타데이터 로그의 리더)는 브로커에서 생성된 모든 RPC를 처리합니다.<br/>
팔로어 컨트롤러는 활성 컨트롤러에 기록된 데이터를 복제하고 활성 컨트롤러에 장애가 발생할 경우 상시 대기 역할을 합니다.<br/>
브로커는 오프셋을 사용하여 KRaft 컨트롤러에 저장된 최신 메타데이터를 추적하므로 메타데이터를 보다 효율적으로 전파하고 컨트롤러 장애 조치로부터 빠르게 복구할 수 있습니다.<br/>
주기적으로 메타데이터의 스냅샷을 디스크에 기록하지만 디스크에서 로그를 다시 읽는 대신 메모리를 상태를 읽어 빠르게 대응이 가능합니다.<br/>

### KRaft의 성능

컨트롤러의 주요 역할은 파티션의 리더를 선출하는 것입니다.<br/>

소수의 파티션에 대한 리더 선출 작업은 카프카 또는 카프카를 사용하는 클라이언트들에게 별다른 영향이 없겠으나, 대량의 파티션에 대한 리더 선출 작업은 다소 시간이 소요되며, 이러한 시간은 대량의 데이터 파이프라인의 역할을 하는 카프카와 클라이언트들에게 매우 크리티컬한 요소일 수 있습니다.<br/>

따라서 이러한 지연 시간을 방지하고자 주키퍼 모드의 경우 카프카 클러스터 전체의 파티션 상한은 약 200,000개 정도였으나, 리더 선출 과정을 개선한 KRaft 모드에서는 훨씬 더 많은 파티션 생성이 가능합니다.<br/>

<img width="770" alt="스크린샷 2024-09-17 오전 5 23 06" src="https://github.com/user-attachments/assets/b75943df-e09d-4a74-853a-aa75d836d60d">

이렇게 속도차이가 나는 이유는 KRaft모드에서의 컨트롤러는 메모리 내에 메타데이터 캐시를 유지하고 있으며, 주키퍼와의 의존성도 제거해 내부적으로 메타데이터의 동기화와 관리과정을 효율적으로 개선했기 때문입니다.<br/>

또한 액티브 컨트롤러 장애 시 최신 메타데이터가 메모리에 유지되고 있으므로, 메타데이터 복제하는 시간도 줄어들어 보다 효율적인 컨트롤러 리더 선출 작업이 일어납니다.<br/>

## set up

`env` 파일과 `docker-compose.yml`을 토대로 kafka 환경을 구성한다.

### config file

- .env
  .env 파일을 만든다.

  ```
  KAFKA_1_HOST=9092
  KAFKA_2_HOST=9093
  KAFKA_3_HOST=9094

  KAFKA_1_PORT=9092
  KAFKA_2_PORT=9093kafka
  KAFKA_3_PORT=9094

  KAFKA_DIR=kafka-data

  KAFKA_CLUSTER_ID=MkU3OEVBNTcwNTJENDM2Qk

  DOCKER_HOST_IP=127.0.0.1

  KAFKA_UI_PORT=8080
  PROFILE=local
  ```

### docker compose file

docker compose 파일을 생성한다. 기존에는 zookeper를 사용하였으나 최신버전 kfak 부터는 zookeeper를 사용하지않고 kraft를 사용한다.<br/>
아파치 카프카 3.7 버전이 주키퍼 모드를 지원하는 마지막 버전이고, 이후 카프카 4.0 버전의 경우는 KRaft 모드로만 사용해야 합니다.<br/>

- **docker-compose-use-zookeeper.yml**
  zookeepser 모드를 사용한 docker compose file이다.

  ```yml
  services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.3.0
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
    ZOOKEEPER_CLIENT_PORT: 2181
    ZOOKEEPER_TICK_TIME: 2000
    volumes:
      - ./log/zookeeper-data:/var/lib/zookeeper/data
      - ./log/zookeeper-log:/var/lib/zookeeper/log
    networks:
      - jpasample-network

  kafka:
    image: confluentinc/cp-kafka:7.3.0
    hostname: kafka
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "29092:29092"
      - "9092:9092"
      - "9101:9101"
    environment:
    KAFKA_BROKER_ID: 1
    KAFKA_ZOOKEEPER_CONNECT: "zookeeper:2181"
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
    KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://127.0.0.1:9092
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
    KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
    KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS: 0
    KAFKA_JMX_PORT: 9101
    KAFKA_JMX_HOSTNAME: localhost
    networks:
      - jpasample-network
  ```

- **docker-compose-use-kraft.yml**
  kraft 모드를 사용한 docker compose file이다.

  ```yml
  services:
  kafka-1:
    container_name: kafka-1
    image: confluentinc/cp-kafka:7.5.3
    ports:
      - "${KAFKA_1_PORT}:9092"
    volumes:
      - ./data/${KAFKA_DIR}/kafka-1:/var/lib/kafka/data
    environment:
    KAFKA_NODE_ID: 1
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
    KAFKA_ADVERTISED_LISTENERS: INTERNAL://:29092,EXTERNAL://${DOCKER_HOST_IP}:${KAFKA_1_PORT}
    KAFKA_LISTENERS: INTERNAL://:29092,CONTROLLER://:29093,EXTERNAL://0.0.0.0:${KAFKA_1_PORT}
    KAFKA_PROCESS_ROLES: "broker,controller"
    KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka-1:29093,2@kafka-2:29093,3@kafka-3:29093
    KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
    KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
    CLUSTER_ID: ${KAFKA_CLUSTER_ID}
    networks:
      - jpasample-network

  kafka-2:
    container_name: kafka-2
    image: confluentinc/cp-kafka:7.5.3
    ports:
      - "${KAFKA_2_PORT}:9093"
    volumes:
      - ./data/${KAFKA_DIR}/kafka-2:/var/lib/kafka/data
    environment:
    KAFKA_NODE_ID: 2
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
    KAFKA_ADVERTISED_LISTENERS: INTERNAL://:29092,EXTERNAL://${DOCKER_HOST_IP}:${KAFKA_2_PORT}
    KAFKA_LISTENERS: INTERNAL://:29092,CONTROLLER://kafka-2:29093,EXTERNAL://0.0.0.0:${KAFKA_2_PORT}
    KAFKA_PROCESS_ROLES: "broker,controller"
    KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka-1:29093,2@kafka-2:29093,3@kafka-3:29093
    KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
    KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
    CLUSTER_ID: ${KAFKA_CLUSTER_ID}
    networks:
      - jpasample-network

  kafka-3:
    container_name: kafka-3
    image: confluentinc/cp-kafka:7.5.3
    ports:
      - "${KAFKA_3_PORT}:9094"
    volumes:
      - ./data/${KAFKA_DIR}/kafka-3:/var/lib/kafka/data
    environment:
    KAFKA_NODE_ID: 3
    KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT
    KAFKA_ADVERTISED_LISTENERS: INTERNAL://:29092,EXTERNAL://${DOCKER_HOST_IP}:${KAFKA_3_PORT}
    KAFKA_LISTENERS: INTERNAL://:29092,CONTROLLER://kafka-3:29093,EXTERNAL://0.0.0.0:${KAFKA_3_PORT}
    KAFKA_PROCESS_ROLES: "broker,controller"
    KAFKA_CONTROLLER_QUORUM_VOTERS: 1@kafka-1:29093,2@kafka-2:29093,3@kafka-3:29093
    KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL
    KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
    CLUSTER_ID: ${KAFKA_CLUSTER_ID}
    networks:
      - jpasample-network
  ```

## kafka 관련 명령어

Docker 컨테이너를 활용하여 kafka 명령어를 실행하는 전제조건으로 기술해놨습니다.

- **현재 Kafka 브로커에서 토픽 목록 조회**
  현재 클러스터에 존재하는 모든 토픽을 확인할 수 있습니다.

  ```sh
  docker exec -it kafka-1 kafka-topics --bootstrap-server kafka-1:29092 --list
  ```

- **새로운 토픽 생성**
  {TOPIC_NAME} 이름의 토픽을 생성합니다. 파티션 수와 복제본 개수를 설정할 수 있습니다.

  ```sh
  docker exec -it kafka-1 kafka-topics --bootstrap-server kafka-1:29092 --create --topic {TOPIC_NAME} --partitions 3 --replication-factor 2
  ```

- **특정 토픽에 메시지 생산(Producer)**
  실행 후 메시지를 입력하면 해당 토픽으로 메시지가 전송됩니다.

  ```sh
  docker exec -it kafka-1 kafka-console-producer --bootstrap-server kafka-1:29092 --topic {TOPIC_NAME}
  ```

- **특정 토픽 메시지 소비(Consumer)**
  {TOPIC_NAME}에서 시작부터 모든 메시지를 소비합니다.

  ```sh
  docker exec -it kafka-1 kafka-console-consumer --bootstrap-server kafka-1:29092 --topic {TOPIC_NAME} --from-beginning
  ```

- **특정 토픽의 상세 정보 확인**
  특정 토픽의 파티션, 복제본 정보 등 상세 내용을 확인할 수 있습니다.

  ```sh
  docker exec -it kafka-1 kafka-topics --bootstrap-server kafka-1:29092 --describe --topic {TOPIC_NAME}
  ```

- **컨슈머 그룹 목록 조회**
  컨슈머 그룹의 목록을 확인할 수 있습니다.

  ```sh
  docker exec -it kafka-1 kafka-consumer-groups --bootstrap-server kafka-1:29092 --list
  ```

- **컨슈머 그룹의 오프셋 정보 조회**
  특정 컨슈머 그룹의 파티션별 오프셋 및 상태를 확인할 수 있습니다.

  ```sh
  docker exec -it kafka-1 kafka-consumer-groups --bootstrap-server kafka-1:29092 --group {GROUP_ID} --describe
  ```

- **토픽 삭제**
  특정 토픽을 삭제합니다.

  ```sh
  docker exec -it kafka-1 kafka-topics --bootstrap-server kafka-1:29092 --delete --topic {TOPIC_NAME}
  ```

## kafka 사용 예시 도메인

다음은 kafka를 활용할 수 있는 예시 도메인들이다. 실시간성이 덜 중요하고, 비동기적 처리가 유리한 도메인에 집중하여 사용하는 것이 좋습니다. 아래의 예시들은 모두 Kafka의 비동기성을 적극적으로 활용할 수 있는 도메인입니다.

### 이메일/알림 발송 시스템

주문이 완료되거나 배송이 완료된 후 고객에게 이메일, 문자, 푸시 알림 등을 보내는 작업은 실시간성이 크게 요구되지 않습니다.

- **Kafka 활용** <br/>
  주문 완료, 결제 완료, 배송 완료 등의 이벤트를 Kafka로 발행하고, 해당 \*\*이벤트를 수신한 소비자(Consumer)가 비동기적으로 이메일이나 알림을 발송합니다.
- **예시** <br/>
  OrderPlacedEvent, PaymentConfirmedEvent, ShipmentCompletedEvent를 발행.
  이를 수신한 서비스에서 고객에게 이메일이나 알림을 보냄.

### 통계 및 로그 수집

사용자의 활동, 주문 기록, 방문 트래픽 등을 실시간으로 DB에 저장할 필요는 없지만, 이후 분석이나 통계 처리에 활용할 수 있습니다.

- **Kafka 활용** <br/>
  사용자가 상품을 조회하거나 주문을 하는 이벤트를 Kafka로 발행하고, 이 데이터를 분석 시스템이나 데이터 웨어하우스로 전달해 통계 처리에 사용합니다.
- **예시** <br/>
  ProductViewedEvent, OrderCompletedEvent 등을 Kafka로 발행하여 데이터 분석을 위한 시스템에 전달. 나중에 상품 조회 빈도, 구매율 등의 통계를 생성.

### 재고 동기화

재고 관리는 실시간 DB 기반으로 처리하되, 다른 외부 시스템과 재고 정보를 동기화하거나 업데이트하는 작업은 비동기로 처리할 수 있습니다.

- **Kafka 활용** <br/>
  상품이 판매될 때마다 Kafka 이벤트로 재고 변경 사항을 발행하고, 이를 수신한 외부 시스템(예: 제3자 판매 채널)에서 재고 상태를 업데이트하도록 처리할 수 있습니다.
- **예시** <br/>
  InventoryUpdatedEvent를 발행하여 재고 변동 사항을 다른 시스템에 전달.

### 고객 리뷰 시스템 (Review Moderation)

고객이 상품 리뷰를 작성할 때, 리뷰가 자동으로 승인이 되거나 검토 후 승인이 되는 구조를 가질 수 있습니다. 리뷰 승인 과정은 즉시 처리되지 않아도 되는 경우가 많습니다.

- **Kafka 활용** <br/>
  리뷰 작성 시 Kafka에 이벤트를 발행하고, 리뷰 검토 후 처리하는 시스템이 비동기적으로 검토 및 승인을 처리할 수 있습니다.
- **예시** <br/>
  ReviewSubmittedEvent를 Kafka로 발행한 후, 관리자 시스템에서 리뷰를 검토하고 승인 여부를 결정.

### 결제 이력 저장

결제가 완료된 후 결제 이력을 다른 저장소에 저장하거나 외부 결제 시스템과 동기화할 수 있습니다.

- **Kafka 활용** <br/>
  결제가 완료된 후 결제 성공 이벤트를 Kafka로 발행하여 결제 기록 저장소나 외부 결제 시스템으로 데이터를 전송합니다.
- **예시**: <br/>
  PaymentCompletedEvent 발행 후 결제 이력을 분석 시스템에 저장하거나 외부 결제 시스템에 전달.

### 배송 추적 시스템

배송이 시작되거나 진행 중일 때, 외부 시스템(예: 배송업체 API)을 통해 배송 상태를 주기적으로 확인하고 업데이트할 수 있습니다. 이 역시 실시간일 필요는 없으므로 Kafka를 활용할 수 있습니다.

- **Kafka 활용** <br/>
  배송 상태 업데이트 이벤트를 Kafka로 발행하여 비동기적으로 배송 추적 정보를 갱신.
- **예시** <br/>
  ShipmentStatusUpdatedEvent를 발행하여 고객에게 배송 상태 업데이트를 제공.

### 카트 상태 저장 (Abandoned Cart Tracking)

고객이 상품을 카트에 담았지만 구매를 완료하지 않았을 때, 카트 상태를 저장하고 나중에 고객에게 리마인더 이메일을 보내는 등의 마케팅 활동을 할 수 있습니다.

- **Kafka 활용** <br/>
  카트에 담긴 상품이 일정 시간 동안 구매되지 않았을 때 Kafka로 이벤트를 발행하고, 이를 마케팅 서비스에서 수신하여 고객에게 리마인더 이메일을 보냅니다.
- **예시** <br/>
  CartAbandonedEvent 발행 후 마케팅 시스템에서 이메일 발송.

[출처]<br/>
https://docs.confluent.io/platform/current/installation/docker/config-reference.html<br/>
https://devocean.sk.com/blog/techBoardDetail.do?page=&boardType=undefined&query=&ID=165711&searchData=&subIndex=&searchText=&techType=&searchDataSub=&searchDataMain= <br/>
https://velog.io/@holicme7/Apache-Kafka-%EC%B9%B4%ED%94%84%EC%B9%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80<br/>
https://medium.com/@0joon/10%EB%B6%84%EC%95%88%EC%97%90-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-kafka-bed877e7a3bc<br/>
