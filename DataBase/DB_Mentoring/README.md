# DB 멘토링

## 1주차(1.11 ~ 1.17)
1.	TEST01과 TEST02의 테이블을 TEST03으로 데이터 통합 진행
대상 테이블은 총 3 개(TBL_LT_INF, TBL_LT_HIS, TBL_LT_DET)
Ex: ) TEST01.TBL_LT_HIS + TEST02.TBL_LT_HIS = TEST03.TBL_LT_HIS

2.	리드멘토가 임의로 PK 중복이 나게 설정했음(일부 데이터만…)
, PK 중복이 나지 않는 경우에는 TEST01, TEST02 
모두 FA_ID가 F12인 경우만 F11로 변환해서 통합

3. 데이터 통합 기준 
TBL_LT_INF -> PK 중복나는 경우에는 TEST01기준

TBL_LT_HIS -> TEST02기준

TBL_LT_DET -> PK 중복나는 경우에는 TEST01기준

4.	STAT_CD 컬럼이 SHIP인 경우 SHIPPED로 변경
, SCRP인 경우 SCRAPPED로 변경, RELE인 경우 RELEASED로 변경해서 통합


## 2주차(1.19 ~ )
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


## 3주차

## 4주차

## 5주차

