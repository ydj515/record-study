insert into TEST03.TBL_LT_DET (
    select * from TEST01.TBL_LT_DET
    union all
    select * from TEST02.TBL_LT_DET b where not exists (
        select * from TEST01.TBL_LT_DET a where
            b.FA_ID = a.FA_ID and
            b.LT_ID = a.LT_ID and
            b.PROD_ID = a.PROD_ID
    )
);

--
INSERT INTO TEST03.TBL_LT_DET
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, PROD_DESC, FL_ID, FL_DESC, OP_ID, OP_DESC, EVENT_DESC, USER_ID
  FROM TEST01.TBL_LT_DET
 UNION ALL
SELECT CASE WHEN FA_ID = 'F12' THEN 'F11' ELSE FA_ID END AS FA_ID
     , LT_ID, PROD_ID, PROD_DESC, FL_ID, FL_DESC, OP_ID, OP_DESC, EVENT_DESC, USER_ID
  FROM TEST02.TBL_LT_DET A
 WHERE NOT EXISTS (
                    SELECT 1
                      FROM TEST01.TBL_LT_DET IA
                     WHERE IA.FA_ID = A.FA_ID
                       AND IA.LT_ID = A.LT_ID
                       AND IA.PROD_ID = A.PROD_ID
                  );
--