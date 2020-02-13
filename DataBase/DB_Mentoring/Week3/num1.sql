SET SERVEROUTPUT ON
CREATE OR REPLACE PROCEDURE SP_FA_IN
IS
    P_OWNER VARCHAR2(40);
    P_TABLE_NAME VARCHAR2(40);
    P_COLUMN_NAME VARCHAR2(40);
    my_query varchar2(200);
BEGIN
    FOR REC1 IN  (
             SELECT *
             FROM ALL_TAB_COLUMNS
             WHERE COLUMN_NAME = 'FA_ID'
            ) 
    LOOP
    
        P_OWNER := REC1.OWNER;
        P_TABLE_NAME := REC1.TABLE_NAME;
        P_COLUMN_NAME := 'FA_ID';
        my_query := 'INSERT INTO HOMEWK_01(TABLE_NAME, COLUMN_NAME, VAL, CNT)';
        my_query := my_query || ' SELECT ' || '''' || P_TABLE_NAME || ''', ''' || P_COLUMN_NAME || ''', ' || 'FA_ID, '  || 'COUNT(*)';
        my_query := my_query || ' FROM ' || P_OWNER || '.' || P_TABLE_NAME;
        my_query := my_query || ' GROUP BY ' || 'FA_ID'; -- group by로 안 묶어주면 Group by로 하라고 나옴
    
        DBMS_OUTPUT.PUT_LINE(my_query);
        EXECUTE IMMEDIATE my_query;
    
   
    END LOOP;
END SP_FA_IN;

EXEC SP_FA_IN; -- 한번에 실행 안되고. 프로시저를 만들고 이문장만 따로 실행해야함


CREATE TABLE HOMEWK_01
(
    TABLE_NAME VARCHAR2(40),
    COLUMN_NAME VARCHAR2(40),
    VAL     VARCHAR2(40),
    CNT     NUMBER(10)
);

SELECT * FROM HOMEWK_01;
DELETE FROM HOMEWK_01;

--INSERT INTO HOMEWK_01(TABLE_NAME, COLUMN_NAME, VAL,CNT) SELECT 'TBL_LT_HIS', 'FA_ID', FA_ID, COUNT(*) FROM TEST03.TBL_LT_HIS group by FA_ID