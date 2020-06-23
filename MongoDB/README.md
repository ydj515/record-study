# MongoDB

## MongoDB
- Document-Oriented(문서 지향적) **NoSQL 데이터베이스**
- 대용량 데이터 서비스에서는 기존의 RDBMS에서 처리하기는 힘들어서 나옴(비용적인 문제 : 데이터 분산을 위해 scale out)
- 자체적으로 분산 처리, 샤딩, 데이터 리밸런싱, 데이터 복제, 복구 등을 지원
- 무엇보다 Schema-Free(Schema-less)한 구조이기에 대용량의 데이터 작업에 아주 효율적인 데이터베이스
- indexing, 내부적으로 B-Tree 자료구조(json과 비슷한 구조)를 이용하여 인덱스를 관리

|MongoDB                           |RDBMS                            |
|----------------------------------|---------------------------------|
|`DataBase`			               |DataBase                         |
|`Collection`          	           |Table                            |
|`Document`         	           |Record                           |
|`Field`         	               |Column                           |
|`index`         	               |index                            |
|`쿼리의 결과로 "커서(Cursor)" 반환` |쿼리의 결과로 "레코드(Record)" 반환|


## 특징
- Document-oriented storage : database > collections > documents 구조로 document는 key-value형태의 BSON(Binary JSON)
- Full Index Support : 다양한 인덱싱을 제공
- Replication& High Availability : 간단한 설정만으로도 데이터 복제를 지원. 가용성 향상.
- Auto-Sharding : MongoDB는 처음부터 자동으로 데이터를 분산하여 저장하며, 하나의 컬렉션처럼 사용할 수 있게 해줌. 수평적 확장 가능
- Querying(documented-based query) : 다양한 종류의 쿼리문 지원. (필터링, 수집, 정렬, 정규표현식 등)
- Fast In-Pace Updates : 고성능의 atomic operation을 지원
- Map/Reduce : 맵리듀스를 지원.(map과 reduce 함수의 조합을 통해 분산/병렬 시스템 운용 지원, 하둡처럼 MR전용시스템에 비해서는 성능이 떨어짐)

### index 종류
- Single Field Indexes: 기본 index
- Compound Indexes: 복합 index
- Multikey Indexes: Array에 미챙되는 값이 하나라도 있으면 인덱스에 추가하는 멀티키 인덱스
- Text Indexes : String에도 인덱싱이 가능
- Hashed Index : Btree 인덱스가 아닌 Hash 타입의 인덱스도 사용 가능

### 장점
- **Flexibility** : Schema-less라서 어떤 형태의 데이터라도 저장할 수 있음
- **Performance** : Read & Write 성능이 뛰어나다. 캐싱이나 많은 트래픽을 감당할 때도 좋음
- **Scalability** : 애초부터 스케일아웃 구조를 채택해서 쉽게 운용가능. Auto sharding 지원
- **Deep Query ability** : 문서지향적 Query Language 를 사용하여 SQL 만큼 강력한 Query 성능을 제공
- **Conversion / Mapping** : JSON형태로 저장이 가능해서 직관적이고 개발이 편리

### 단점
- **table JOIN이 없어서** join이 필요없도록 데이터 구조화 필요
- 메모리 관리를 OS에게 위임한다. **메모리에 의존적**, 메모리 크기가 성능에 영향이 큼
- SQL을 완전히 이전할 수는 없다.
- B트리 인덱스를 사용하여 인덱스를 생성하는데, **B트리는 크기가 커질수록 새로운 데이터를 입력하거나 삭제할 때 성능 저하**
- 이런 B트리의 특성 때문에 데이터를 넣어두면 변하지않고 정보를 **조회하는 데에 적합**




[출처]  
https://coding-start.tistory.com/273  