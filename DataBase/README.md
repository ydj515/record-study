# DataBase

- **7daySQL Challenge :** https://github.com/ydj515/record-study/tree/master/DataBase/7daySQL

- **DB 멘토링 :** https://github.com/ydj515/record-study/tree/master/DataBase/DB_Mentoring

## Oracle 설치
### Window
1. Oracle Database 12c Release 1 (12.1.0.2.0) - Enterprise Edition
- file 1,2 둘다 설치  
- https://www.oracle.com/database/technologies/oracle-database-software-downloads.html

2. SQL Developer
- https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html

<img width="1404" alt="스크린샷 2020-01-11 오후 1 03 26" src="https://user-images.githubusercontent.com/32935365/72321422-30a9c880-36e7-11ea-8926-5a4b34c6bcdd.png">


### Mac

1. Docker 설치

2. Docker Oracle Database image down
- docker에 설치 하고 싶은 이미지를 docker에서 검색하여 다운로드

```
docker pull store/oracle/database-enterprise:12.2.0.1
```

- 이미지 다운 확인
```
docker images
```

- Oracle 실행  
store/oracle/database-enterprise:12.2.01.의 docker image를 local_db라는 이름으로 프로세스를 실행  
```
docker run -dit --name local_db -p 1521:1521 store/oracle/database-enterprise:12.2.0.1
```

- Docker에서 Oracle 실행 확인
```
docker ps
```
![docker ps](https://user-images.githubusercontent.com/32935365/72321436-3acbc700-36e7-11ea-8508-25e989a770f6.png)  


- 포트 확인
```
lsof -PiTCP -sTCP:LISTEN
```
![포트 listen](https://user-images.githubusercontent.com/32935365/72321451-46b78900-36e7-11ea-9939-47f2ccef895a.png)  


- Docker Oracle 중지
```
docker stop local_db
```

- Docker Oracle 재시작
```
docker restart local_db
```

- SQL Plus 접속  
sys as sysdba로 접속해야함!!
```
docker exec -it local_db bash -c "source /home/oracle/.bashrc; sqlplus sys/Oradoc_db1@ORCLCDB as sysdba"
```
![sql 접속](https://user-images.githubusercontent.com/32935365/72321463-4f0fc400-36e7-11ea-855b-2f1ed8ce6829.png)  

3. SQL Developer
- https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html
- 설정 저장 후 테스트 후 접속
![sql developer 연동](https://user-images.githubusercontent.com/32935365/72321487-5c2cb300-36e7-11ea-8be1-f64dcc256b37.png)  

- **실행계획으로 Join이 몇번 일어났는지 확인할 수 있다!**


- Oracle 서버와 연동

## 특이 사항
### Sysdba 임에도 불구하고 create user가 안되는 경우
- Oracle 12c 버전은 명명 규칙이 너무 까다로워서 그럴 때가 있다.
- 해결방법
    1. user 앞에 c##을 붙힌다
    ```
    create c##user aaa indentified by 'aaa'
    ```
    2.  원래 기존 처럼 편하게 생성 가능(이게 베스트)
    ```
    ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;
    ```

### SQL Developer가 접속이 안되는 경우
- Docker가 실행되어 있지 않은 경우 => 첫 부팅 시 WIFI가 없어서 실행이 안되어있을 수 있음
- Docker는 실행되어 있지만 Oracle이 실행되어 있지 않은 경우 => 터미널에서 "docker ps" 명령어로 확인!

## ORACLE 배운것

### 논리적 저장 구조
- http://www.gurubee.net/lecture/1480
- table space > segment > extent > block
- block : rowid(행을 나타내는 주소값. 속도가 제일 빠름) + data

### 물리적 저장구조
- data file

### 3S
- Syntax : 문법 검사
- Semantic : 의미검사
- Security : 접근권한

### SQL 실행 순서
- 예약어 실행 순서
```sql 
FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY
```
### 실행계획 
syntax -> semantic -> security -> parse -> execute -> fetch(select만)  
- 이미 수행한 SQL문의 경우 shared pool에 저장(처음부터 끝까지 토시하나 안틀리고 같아야함)
``` sql
SELECT *
FROM A
WHERE a=1 AND b=22;
```

``` sql
SELECT *
FROM A
WHERE b=2 AND a=1;
```
- 위와 같이 극단적으로 같은 결과지만 WHERE 구문의 순서가 바뀌므로 hardparsing이 일어남. 심지어 대소문자도 같아야함.
- 바인드 변수 처리를 통해 softparsing을 유도하여 syntax, semantic, security의 과정 생략 가능  

parse 단계에서 2가지로 나뉨  
- hardparsing  
위의 전 과정을 모두 실행

- softparsing  
execute feth만 실행  
shared pool에 sql 실행 된 정보를 토대로 
```sql
where aname = :a
```
와 같이 바인드 변수 처리면 처음 실행 1회시에만 hardparsing을 하고 그 다음부턴 softparsing.  
jdbc 커넥션 할 때 server에서 값을 넣어주어 softparsing을 유도.

- 실행계획 확인
- 밑의 쿼리문을 실행하면 몇번 째 파티션을 타는지 볼 수 있음.
```sql
explain partitions -- 파티션들에 대한 실행계획 확인
select * from test
where REG_DT between '2020-04-08 00:00' and '2020-04-08 23:59'; -- 하루치. 24:00으로 하면 절대 안나옴
```

### Merge
- table에 row를 조건적으로 insert또는 update(update와 insert를 결합문)
- MERGE를 실행하는 user는 해당 table에 insert와 update를 할 수 있는 권한이 있어야함.
- **INTO** : data가 update되거나 insert될 table name (emp_history는 target table)
- **USING** : 대상 table의 data와 비교한 후 update또는 insert할 때 사용할 data의 source (emp는 source table)
- **ON** : update나 insert할 condition으로, 해당 condition을 만족하는 row가 있으면 WHEN MATCHED 이하를 실행, 없으면 WHEN NOT METCHED 이하를 실행
- **WHEN MATCHED** : ON의 조건이 TRUE인 row에 수행할 내용
- **WHEN NOT MATCHED** : ON의 조건에 맞는 row가 없을 때 수행할 내용

- 예시 
```sql
MERGE INTO emp_history eh
USING emp 
ON (e.empno = eh.empno)  
WHEN MATCHED THEN
    UPDATE SET eh.salary = e.sal
WHEN NOT MATCHED THEN
    INSERT VALUES (e.empno, sysdate, sal);
```

### UNION ALL vs UNION
- UNION은 조인은 정렬을 하기 때문에 느림
- UNION ALL은 정렬을 하지 않으므로 빠름 => UNION ALL을 써야함

### WITH
- 임시 테이블
- 동일한 SQL이 반복되어서 사용될 때 성능을 높이기 위해 사용
- WITH 테이블이름 as (데이터)
```sql
WITH R AS (
    SELECT A.FA_ID      AS  FA_ID_M1,
           A.LT_ID      AS  LT_ID_M1,
           A.PROD_ID    AS PROD_ID_M1,
           A.TIMEKEY    AS TIMEKEY_M1,
           A.FL_ID      AS FL_ID_M1,
           A.OP_ID      AS OP_ID_M1,
           A.STAT_CD    AS STAT_CD_M1,
           A.STAT_TYP   AS STAT_TYP_M1,
           
           B.FA_ID      AS    FA_ID_M2,
           B.LT_ID      AS  LT_ID_M2,
           B.PROD_ID    AS PROD_ID_M2,
           B.TIMEKEY    AS TIMEKEY_M2,
           B.FL_ID      AS FL_ID_M2,
           B.OP_ID      AS OP_ID_M2,
           B.STAT_CD    AS STAT_CD_M2,
           B.STAT_TYP   AS STAT_TYP_M2
    FROM TEST01.TBL_LT_HIS A

    FULL OUTER JOIN
        TEST02.TBL_LT_HIS B
    ON A.FA_ID = B.FA_ID
        AND A.LT_ID = B.LT_ID
        AND A.PROD_ID = B.PROD_ID
        AND A.TIMEKEY = B.TIMEKEY
)
```

## OUTER JOIN
- 데이터가 없을 수도 있는 쪽 JOIN 컬럼에 (+)를 추가하여 OUTER JOIN이 가능  
![outer join](https://user-images.githubusercontent.com/32935365/74147646-047e5a80-4c47-11ea-9ad7-1ea8162249b3.PNG)

### Join
1. NL(Nested Loops) Join
- for loop 2개
- 선행 테이블의 index가 필수
- random data access를 하므로 데이터가 적을 때 유리
- 온라인 프로그램에 적당

2. Hash Join
- equal join만 가능 (=)
- 속도가 제일 빠름
- Hash table이 oracle temporary영역(임시 테이블이 있는 곳)에 잡힘.
- Hash table 생성하는 시간은 좀 오래 걸릴 수도 있음

=> 데이터가 적은 경우에는 NL Join과 Hash Join 어떤 것을 쓰는것이 좋을까?
=> NL Join을 쓴다. 이유는 데이터가 적은 경우 NL과 Hash 모두 빠르기 때문이다. 또한, temporary영역에 다른 임시 테이블이 많다면 Hash table 생성하고 수행하는 것 보다 NL Join 사용하는 편이 좋음
=> 임시영역이 모두 차거나 많은 공간이 차 버리면 DB 자체가 뻗어 버릴 수 있는 위험이 있기 때문이기도 하다.

3. Sort Merge
- 데이터 양이 많을 때 사용

## partitioning
- 큰 테이블이나 인덱스를 관리하기 쉬운 단위로 분리하는 방법을 의미
- partition된 테이블은 fk를 지원 x
- 테이블이 unique 또는 PK를 가지고 있다면, 파티션 키는 모든 unique 또는 PK의 일부 또는 모든 컬럼을 포함해야 함
- 기준이 퇴는 컬럼은 반드시 PK로 지정되어 있어야 함
- 장점 :  DML query(특히 insert, update, delete와 같은 write query)의 성능을 향상시킴. 특히 OLTP 시스템에서 insert작업들을 분리된 파티션을 분산시켜 경합을 줄임
- 단점 : Table Join에 대한 비용이 증가. 테이블과 인덱스를 별도로 파티션 할 수 없음. 테이블과 인덱스를 같이 partitioning해야함
- table의 컬럼이 DATETIME일 경우 DATE로 바꾸어서 insert해줘야하므로 TO_DAYS를 사용
- 파티션이 포함할 수 없는 데이터(범위보다 작거나 큰 데이터)가 있다면 Table has no partition for value 788465 와 같은 데이터가 나옴

### 예시
- 파티션 생성
```sql
-- 날짜 별로 파티션 생성
ALTER TABLE test PARTITION BY RANGE(TO_DAYS(REG_DT))( 
  PARTITION p1 VALUES LESS THAN (TO_DAYS('2020-04-08')),
  PARTITION p2 VALUES LESS THAN (TO_DAYS('2020-04-09')),
  PARTITION p3 VALUES LESS THAN (TO_DAYS('2020-04-10')),
  PARTITION p4 VALUES LESS THAN (TO_DAYS('2020-04-11'))
 );

```
- 파티션 내용 조회
```sql
-- 파티션p2의 내용 조회
SELECT * FROM test PARTITION(p2);
```

- 해당 테이블 파티션 완전 삭제
```sql
-- test 테이블의 모든 파티션 삭제
ALTER TABLE test REMOVE PARTITIONING;
```

- 해당 파티션 삭제
```sql
-- 해당 테이블에 대한 해당 파티션 삭제
ALTER TABLE `테이블` DROP PARTITION `파티션명1`;
```

### range paritioning
- 기간을 기준으로 하여 range를 나눔
- 연도별
```sql
PARTITION BY RANGE (YEAR(`REG_DT`))
```
- 일(월)별
```sql
PARTITION BY RANGE (TO_DAYS(`REG_DT`))
```

### list paritioning

### composite paritioning

### Hash paritioning

### Horizontal paritioning

## Index
- 기존 테이블에 몇개의 필드만 가지고 있는 테이블
- 조회(select)시간을 단축 시킬 수 있다.
- index를 쓰면 조회가 빨라질 수 있지만, DML이 느려진다.
- index를 여러개 만들면 기존 테이블보다 차지하는 공간이 많아 질 수 있다.
- 예시
A테이블의 필드가 a, b, c, d를 가지고 있다.  
index A*의 필드를 a, b로 만든다면
이 때, order by a, b로 진행 되기 때문에 index에서 select를 할 경우 a필드를 먼저 지정해주어야 한다.
```sql
select a
from A*
where a=1, b=2
;
```
만약 아래와 같이 select를 한다면 결과는 동일하지만  
a로 우선 정렬이 되있기 때문에 index를 사용하여 select하는 것이 더 느릴 뿐 아니라 의미 자체가 없어진다.
```sql
select a
from A*
where b=2, a=1
;
```
따라서 항상 index를 사용할 경우 첫 필드를 지정을 해주어야 한다. 누락해도 select 성능이 떨어진다.

그러나, 아래와 같이 * 을 조회할 경우 다시 A 테이블로 가서 rowid를 가지고 나머지 필드 c, d값을 조회하기 때문에 의미가 없다.
```sql
select *
from A*
where b=2, a=1
;
```

### 예시
- 파티션 인덱스하기
```sql
CREATE INDEX index01 ON test(REG_DT); // local index를 만드는 경우
```

- 해당 테이블 index 조회
```sql
SHOW INDEX FROM test
```

- 해당 인덱스 삭제
```sql
ALTER TABLE test DROP INDEX index01;
```

## PROCEDURE
- 특정 로직만 처리하고 결과 값을 반환하지 않는 서브 프로그램
- 함수 느낌
- 프로시저만 실행해서 한번에 처리하게 끔 만듬
- https://logical-code.tistory.com/48

```sql
CREATE OR REPLACE PROCEDURE 프로시저이름
    ( 매개변수1 [IN|OUT|IN OUT] 데이터타입 [:= 디폴트값]
      매개변수2 [IN|OUT|IN OUT] 데이터타입 [:= 디폴트값]
    )
    IS[AS]
        -- 프로시저 내부에서 사용할 변수 선언
        변수명 데이터타입
    BEGIN
        실행부
END 프로시저이름;
```

- 프로시저 안엣 쿼리문을 동적으로 만들 수 있다.
- || 로 연결
```sql
my_query := my_query || ' SELECT ' || '''' || P_TABLE_NAME || ''', ''' || P_COLUMN_NAME || ''', ' || 'FA_ID, '  || 'COUNT(*)';
my_query := my_query || ' FROM ' || P_OWNER || '.' || P_TABLE_NAME;
```

## 참고
### unique key 설정
```sql
ALTER TABLE MWS_COLT_NEWS ADDUNIQUE UK_AID (AID); // unique key 설정. varchar 191까지만 가능하다. 
```
### CASCADE
- news table(부모) 컬럼 삭제하면 info table(자식, fk 설정되어 있는 곳) 해당 컬럼들도 삭제
1. 기존 제약 조건 삭제
```sql
ALTER TABLE MWS_COLT_NEWS_INFO DROP CONSTRAINT MWS_COLT_NEWS_INFO_ibfk_1;
ALTER TABLE MWS_COLT_NEWS_INFO DROP FOREIGN KEY MWS_COLT_NEWS_INFO_ibfk_1;
```

2. CASCADE 옵션 설정
아래와 같이 DELETE 와 UPDATE를 모두 설정해 주어야 data insert가 된다.
```sql
-- 대부분의 경우 DELETE만 걸어준다. 
ALTER TABLE MWS_COLT_NEWS_INFO ADD CONSTRAINT FOREIGN KEY (NEWS_ID) REFERENCES MWS_COLT_NEWS(ID) ON DELETE CASCADE;
ALTER TABLE MWS_COLT_NEWS_INFO ADD CONSTRAINT FOREIGN KEY (NEWS_ID) REFERENCES MWS_COLT_NEWS(ID) ON UPDATE CASCADE;
```

### history table에 대한 PK 설정
- history table의 id(auto_increment), log_date의 컬럼일 경우 pk는 id, id+log_date, log_date+id 의 3가지 경우이다.
- 보통 select할 경우 날짜 범위로 검색을 하기 때문에(point query가 아닌 range query) index를 만들 경우 log_date+id의 선택이 효율이 좋다.
- 즉 날짜 컬럼이 PK의 첫번째 컬럼인 것이 좋다.





[출처]  
https://blog.naver.com/qor3326/220934450444  
https://wookoa.tistory.com/239 [Wookoa]  
https://forgiveall.tistory.com/352 [하하하하하]  
http://www.gurubee.net/  
https://jwchoi85.tistory.com/86  
https://logical-code.tistory.com/48  
https://gent.tistory.com/39  
https://nesoy.github.io/articles/2018-02/Database-Partitioning  
https://purumae.tistory.com/211  
https://coding-factory.tistory.com/422  
http://www.gurubee.net/lecture/1914  
https://jack-of-all-trades.tistory.com/79  