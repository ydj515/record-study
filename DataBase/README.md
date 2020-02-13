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





[출처]  
https://blog.naver.com/qor3326/220934450444  
https://wookoa.tistory.com/239 [Wookoa]  
https://forgiveall.tistory.com/352 [하하하하하]  
http://www.gurubee.net/  
https://jwchoi85.tistory.com/86  
https://logical-code.tistory.com/48  
https://gent.tistory.com/39