insert into TEST03.TBL_LT_HIS (
    select * from TEST02.TBL_LT_HIS
    union all
    select * from TEST01.TBL_LT_HIS b where not exists (
        select * from TEST02.TBL_LT_HIS a where
            b.FA_ID = a.FA_ID and
            b.LT_ID = a.LT_ID and
            b.PROD_ID = a.PROD_ID
    )
);

--
INSERT INTO TEST03.TBL_LT_HIS
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, TIMEKEY, FL_ID, OP_ID
     , CASE WHEN STAT_CD = 'SHIP' THEN 'SHIPPED'
            WHEN STAT_CD = 'SCRP' THEN 'SCRAPPED'
            WHEN STAT_CD = 'RELE' THEN 'RELEASED' END AS STAT_CD
     , STAT_TYP
  FROM TEST01.TBL_LT_HIS
 UNION ALL
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, TIMEKEY, FL_ID, OP_ID
     , CASE WHEN STAT_CD = 'SHIP' THEN 'SHIPPED'
            WHEN STAT_CD = 'SCRP' THEN 'SCRAPPED'
            WHEN STAT_CD = 'RELE' THEN 'RELEASED' END AS STAT_CD
     , STAT_TYP
  FROM TEST02.TBL_LT_HIS A
 WHERE NOT EXISTS (
                    SELECT 1
                      FROM TEST01.TBL_LT_HIS IA
                     WHERE IA.FA_ID = A.FA_ID
                       AND IA.LT_ID = A.LT_ID
                       AND IA.PROD_ID = A.PROD_ID
                  );
--