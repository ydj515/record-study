# Elasticsearch

## What is Elasticsearch
- 뛰어난 검색기능
- 대규모 분산 시스템을 구축할 수 있게 많은 기능 지원
- Full Text Search(전문 검색), 문서의 점수화를 이용한 정렬, 실시간 검색(Real Time)

### 실시간 분석
- 엘라스틱서치에 저장된 데이터는 검색에 사용되기 위해 별도의 재시작 or 상태의 개인이 필요x

### 분산 시스템
- 시스템의 규모가 늘어나면 기존 노드에 새 노드를 실행해 연결하는 것으로 쉽게 시스템 확장 가능
- 데이터는 각 노드에 분산 저장되고 복사본을 유지해 각종 충돌로부터 노드 데이터의 유실을 방지
- 노드 : 데이터를 색인하고 검색 기능을 수행하는 엘라스틱서치의 단위 프로세스

### 높은 가용성
- 각 노드는 1개이상의 데이터 원본과 복사본을 서로 다른 위치에 저장
- 노드의 상태 이상이 있을 경우 안전성 보장 가능

### Multi Tenancy
- 데이터를 검색할 때 서로 다른 인덱스의 데이터를 바로 하나의 질의로 묶어 검색
- 여러 검색 결과를 하나의 출력으로 도출

### Full Text Search(전문 검색)
- 데이터의 전체 문장에서 검색어를 추출해 저장
- 이를 바탕으로 검색하는 전문 검색 지원

### JSON 문서 기반
- JSON구조로 저장되어 모든 레벨의 필드에 접근이 쉽고, 매우 빠른 속도로 검색

### RESTFul API
- URI를 사용한 동작 가능
- GET, POST, PUT, DELETE
- -d 옵션(data)를 주고 작은 따옴표안에 JSON으로 데이터 삽입
```
curl -X{메소드} http://{호스트}:{포트}/{인덱스}/{타입}/{도큐먼트 id} -d '{데이터}'
```

### RDB vs. Elasticsearch
|관계형 DB          |Elasticsearch                  |
|------------------|-------------------------------|
|데이터베이스(DB)    |인덱스(index)                  |
|테이블(Table)       |타입(type)                    |
|행(Row)            |도큐먼트(document)             |
|열(Column)         |필드(field)                    |
|스키마(schema)     |매핑(mapping)                  |


http://localhost:9200

## Logstash

## Kibana
http://localhost:5601

[출처]  
https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221179410434&proxyReferer=https%3A%2F%2Fwww.google.com%2F  

- 윈도우 설치  
https://lng1982.tistory.com/283