INSERT INTO TEST03.TBL_LT_HIS(
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

SELECT * FROM (

-- TEST01 is NULL
    SELECT FA_ID_M2     AS FA_ID,
           LT_ID_M2     AS LT_ID,
           PROD_ID_M2   AS PROD_ID,
           TIMEKEY_M2   AS TIMEKEY,
           FL_ID_M2     AS FL_ID,
           OP_ID_M2     AS OP_ID,
           STAT_CD_M2   AS STAT_CD,
           STAT_TYP_M2  AS STAT_TYP
    FROM R
    WHERE FA_ID_M1 IS NULL AND
          LT_ID_M1 IS NULL AND
          PROD_ID_M1 IS NULL AND
          TIMEKEY_M1 IS NULL -- PK가 NULL인 경우
        
    UNION ALL
    
-- TEST02 is NULL
    SELECT FA_ID_M1     AS FA_ID,
           LT_ID_M1     AS LT_ID,
           PROD_ID_M1   AS PROD_ID,
           TIMEKEY_M1   AS TIMEKEY,
           FL_ID_M1     AS FL_ID,
           OP_ID_M1     AS OP_ID,
           STAT_CD_M1   AS STAT_CD,
           STAT_TYP_M1  AS STAT_TYP
    FROM R
    WHERE FA_ID_M2 IS NULL AND
          LT_ID_M2 IS NULL AND
          PROD_ID_M2 IS NULL AND
          TIMEKEY_M2 IS NULL -- PK가 NULL인 경우

    UNION ALL
    
-- TBL_LT_HIS -> PK 중복나는 경우에는 
-- 조건1
-- TEST01   TEST02
-- PROCESS  PROCESS -> TEST01 insert
-- SELECT   SELECT  -> TEST01 insert
-- LOADING  LOADING -> TEST01 insert
-- RESERVE  RESERVE -> TEST01 insert
    
-- 조건2
-- TEST01쪽 data insert
    SELECT FA_ID_M1     AS FA_ID,
           LT_ID_M1     AS LT_ID,
           PROD_ID_M1   AS PROD_ID,
           TIMEKEY_M1   AS TIMEKEY,
           FL_ID_M1     AS FL_ID,
           OP_ID_M1     AS OP_ID,
           STAT_CD_M1   AS STAT_CD,
           STAT_TYP_M1  AS STAT_TYP
    FROM R
    WHERE (
	    (STAT_TYP_M1 = STAT_TYP_M2) AND
        (STAT_TYP_M1 = 'RESERVE' AND STAT_TYP_M2 = 'LOADING') OR
        (STAT_TYP_M1 = 'SELECT' AND STAT_TYP_M2 = 'PROCESS') OR
        (STAT_TYP_M1 = 'PROCESS' AND STAT_TYP_M2 = 'RESERVE') OR
        (STAT_TYP_M1 = 'LOADING' AND STAT_TYP_M2 = 'SELECT')
    )
    
    UNION ALL
    
-- 조건2
-- TEST02쪽 data insert
    SELECT FA_ID_M2     AS FA_ID,
           LT_ID_M2     AS LT_ID,
           PROD_ID_M2   AS PROD_ID,
           TIMEKEY_M2   AS TIMEKEY,
           FL_ID_M2     AS FL_ID,
           OP_ID_M2     AS OP_ID,
           STAT_CD_M2   AS STAT_CD,
           STAT_TYP_M2  AS STAT_TYP
    FROM R
    WHERE (
	    (STAT_TYP_M1 = STAT_TYP_M2) AND
        (STAT_TYP_M2 = 'RESERVE' AND STAT_TYP_M1 = 'LOADING') OR
        (STAT_TYP_M2 = 'SELECT' AND STAT_TYP_M1 = 'PROCESS') OR
        (STAT_TYP_M2 = 'PROCESS' AND STAT_TYP_M1 = 'RESERVE') OR
        (STAT_TYP_M2 = 'LOADING' AND STAT_TYP_M1 = 'SELECT')
    )
))