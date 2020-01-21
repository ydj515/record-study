insert into TEST03.TBL_LT_INF (
    select * from TEST01.TBL_LT_INF
    union all
    select * from TEST02.TBL_LT_INF b where not exists (
        select * from TEST01.TBL_LT_INF a where
            b.FA_ID = a.FA_ID and
            b.LT_ID = a.LT_ID and
            b.PROD_ID = a.PROD_ID)
);

--
INSERT INTO TEST03.TBL_LT_INF
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, FL_ID, OP_ID, TIMEKEY, CHG_TM, CRT_TM
  FROM TEST01.TBL_LT_INF
 UNION ALL
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, FL_ID, OP_ID, TIMEKEY, CHG_TM, CRT_TM
  FROM TEST02.TBL_LT_INF A
 WHERE NOT EXISTS (
                    SELECT 1
                      FROM TEST01.TBL_LT_INF IA
                     WHERE IA.FA_ID = A.FA_ID
                       AND IA.LT_ID = A.LT_ID
                       AND IA.PROD_ID = A.PROD_ID
                  );
--