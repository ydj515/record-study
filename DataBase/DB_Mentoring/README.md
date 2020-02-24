# DB 멘토링

## 1주차(1.11 ~ 1.17)
1. TEST01과 TEST02의 테이블을 TEST03으로 데이터 통합 진행
대상 테이블은 총 3 개(TBL_LT_INF, TBL_LT_HIS, TBL_LT_DET)
Ex: ) TEST01.TBL_LT_HIS + TEST02.TBL_LT_HIS = TEST03.TBL_LT_HIS

2. 리드멘토가 임의로 PK 중복이 나게 설정했음(일부 데이터만…)
, PK 중복이 나지 않는 경우에는 TEST01, TEST02 
모두 FA_ID가 F12인 경우만 F11로 변환해서 통합

3. 데이터 통합 기준 
TBL_LT_INF -> PK 중복나는 경우에는 TEST01기준

TBL_LT_HIS -> TEST02기준

TBL_LT_DET -> PK 중복나는 경우에는 TEST01기준

4. STAT_CD 컬럼이 SHIP인 경우 SHIPPED로 변경
, SCRP인 경우 SCRAPPED로 변경, RELE인 경우 RELEASED로 변경해서 통합


## 2주차(1.19 ~ 2.8)
1. TBL_LT_HIS 통합 -> PK 중복안나는 경우는 그냥 해당 데이터넣기  

2. PK 중복나는 경우 아래 기준 참고해서 작성

TBL_LT_HIS -> PK 중복나는 경우에는  
RESERVE	LOADING         -> RESERVE우선  
PROCESS	PROCESS		-> TEST01 기준  
SELECT	PROCESS		-> SELECT 우선  
SELECT	SELECT		-> TEST01 기준  
LOADING	LOADING		-> TEST01 기준  
PROCESS	RESERVE		-> PROCESS 우선  
RESERVE	RESERVE		-> TEST01 기준  
LOADING	SELECT		-> LOADING 기준  

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
) --WITH END
```


## 3주차(2.9 ~ 2.15)
1. FA_ID 컬럼이 들어간 모든 테이블에 대해서 DISTINCT한 FA_ID 값과, 개수를 조사한다.

2. 개수를 조사할때에는 Dictionary View를 활용하며, PL / SQL을 활용한 프로시저를 개발해서 조사를 수행한다 ( Dictionary View = ALL_TAB_COLUMNS 활용)

3. 조사한 결과를 테이블에 담는다 (테이블명은 HOMEWK_01로 통일)
CREATE TABLE HOMEWK_01
(
TABLE_NAME VARCHAR2(40),
COLUMN_NAME VARCHAR2(40),
VAL     VARCHAR2(40),
CNT     NUMBER(10));

4. 프로시저에서 바로 HOMEWK_01로 조사한 결과를 INSERT해 결과를 추출한다.

```sql
create or replace PROCEDURE SP_FA_IN AS 
BEGIN
  FOR REC1 IN  (
            SELECT * FROM ALL_TAB_COLUMNS
            ) 
    LOOP
   
    DBMS_OUTPUT.PUT_LINE(REC1.TABLE_NAME);
   
    END LOOP;
END SP_FA_IN;
```

## 4주차(2.16 ~ 2.22)
1. TEST01.TBL_LT_INF 테이블의 PROD_ID 중 일부 PROD_ID를 변환해 통합 요구사항 발생

2. 테이블 조인을 통해 TBL_PROD_INFMAPP의 PROD_YN이 'Y'이고 FA_ID, LT_ID, PROD_ID가 TBL_LT_INF와 같은 경우 TBL_LT_INF의 PROD_ID를 TBL_PROD_INFMAPP의 MAIN_PROD_ID로 변환해서 통합

3. TBL_LT_INF의 PROD_ID가 TBL_PROD_INFMAPP에 없는 경우는 TBL_LT_INF의 PROD_ID값으로 유지

4. 양쪽 테이블의 PROD_ID를 MAIN 제품으로 매핑한 이후에 PK 중복나는 경우에는 TEST01위주로 통합

```sql
CREATE TABLE TEST01.TBL_PROD_INFMAPP
(
    FA_ID       VARCHAR2(50),
    LT_ID       VARCHAR2(50),
    PROD_ID     VARCHAR2(50) ,
    MAIN_PROD_ID  VARCHAR2(50),
    PROD_YN       VARCHAR2(10)
);

CREATE UNIQUE INDEX TEST01.TBL_PROD_INFMAPP_PK
ON TEST01.TBL_PROD_INFMAPP(FA_ID, LT_ID, PROD_ID);

ALTER TABLE TEST01.TBL_PROD_INFMAPP ADD CONSTRAINT TBL_PROD_INFMAPP_PK PRIMARY KEY(FA_ID, LT_ID, PROD_ID);

INSERT INTO TEST01.TBL_PROD_INFMAPP
SELECT FA_ID
     , LT_ID
     , PROD_ID
     , PROD_ID || '_MAIN'
     , CASE WHEN MOD(ROWNUM, 2)  = 1 THEN 'Y'
     ELSE 'N'
     END AS PROD_YN
  FROM TEST01.TBL_LT_INF
 WHERE ROWNUM <= 5000
  ;
  
INSERT INTO TEST01.TBL_PROD_INFMAPP
SELECT FA_ID
     , LT_ID
     , PROD_ID
     , PROD_ID || '_MAIN'
     , CASE WHEN MOD(ROWNUM, 3)  = 1 THEN 'Y'
     ELSE 'N'
     END AS PROD_YN
  FROM TEST02.TBL_LT_INF
 WHERE ROWNUM <= 10000
  ;
  
COMMIT;
```

