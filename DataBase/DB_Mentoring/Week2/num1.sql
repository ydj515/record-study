WITH R AS (
            SELECT A.FA_ID  AS    FA_ID_M1  
                 , A.LT_ID    AS  LT_ID_M1
                 , A.PROD_ID    AS PROD_ID_M1
                 , A.TIMEKEY    AS TIMEKEY_M1
                 , A.FL_ID      AS FL_ID_M1
                 , A.OP_ID      AS OP_ID_M1
                 , A.STAT_CD    AS STAT_CD_M1
                 , A.STAT_TYP   AS STAT_TYP_M1
                 , B.FA_ID  AS    FA_ID_M2  
                 , B.LT_ID    AS  LT_ID_M2
                 , B.PROD_ID    AS PROD_ID_M2
                 , B.TIMEKEY    AS TIMEKEY_M2
                 , B.FL_ID      AS FL_ID_M2
                 , B.OP_ID      AS OP_ID_M2
                 , B.STAT_CD    AS STAT_CD_M2
                 , B.STAT_TYP   AS STAT_TYP_M2
              FROM TEST01.TBL_LT_HIS A
              FULL OUTER JOIN
                   TEST02.TBL_LT_HIS B
                ON A.FA_ID = B.FA_ID
               AND A.LT_ID = B.LT_ID
               AND A.PROD_ID = B.PROD_ID
               AND A.TIMEKEY = B.TIMEKEY
            )
-- 여기서부터 코드 작성하시면됩니다.