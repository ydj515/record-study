CREATE TABLE student (
	S_ID VARCHAR(50) primary KEY,
	S_NM VARCHAR(50)
);
--

CREATE TABLE course (
	C_ID VARCHAR(50) primary KEY,
	C_NM VARCHAR(50)
);
--

CREATE TABLE study (
	S_ID VARCHAR(50),
	C_ID VARCHAR(50),
	CHASU INT,
	FOREIGN KEY(S_ID) REFERENCES student(S_ID),
	FOREIGN KEY(C_ID) REFERENCES course(C_ID)
);
--

INSERT INTO student(S_ID, S_NM) VALUES("001","기민용");
INSERT INTO student(S_ID, S_NM) VALUES("002","이현석");
INSERT INTO student(S_ID, S_NM) VALUES("003","김정식");
INSERT INTO student(S_ID, S_NM) VALUES("004","강정식");

INSERT INTO course(C_ID, C_NM) VALUES("001","Database");
INSERT INTO course(C_ID, C_NM) VALUES("002","Java");

INSERT INTO study(S_ID, C_ID, CHASU) VALUES("001","001", 1);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("001","001", 3);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("001","002", 2);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("002","001", 1);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("002","001", 2);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("002","001", 3);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("003","002", 1);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("003","002", 2);
INSERT INTO study(S_ID, C_ID, CHASU) VALUES("004","001", 1);

--

WITH student AS
(
    SELECT '001' s_id, '기민용' s_nm FROM dual
    UNION ALL SELECT '002', '이현석' FROM dual
    UNION ALL SELECT '003', '김정식' FROM dual
    UNION ALL SELECT '004', '강정식' FROM dual
)
, course AS
(
    SELECT '001' c_id, 'Database' c_nm FROM dual
    UNION ALL SELECT '002', 'Java' FROM dual    
)
, study AS
(
    SELECT '001' s_id, '001' c_id, 1 chasu FROM dual
    UNION ALL SELECT '001', '001', 3 FROM dual
    UNION ALL SELECT '001', '002', 2 FROM dual
    UNION ALL SELECT '002', '001', 1 FROM dual
    UNION ALL SELECT '002', '001', 2 FROM dual
    UNION ALL SELECT '002', '001', 3 FROM dual
    UNION ALL SELECT '003', '002', 1 FROM dual
    UNION ALL SELECT '003', '002', 2 FROM dual
    UNION ALL SELECT '004', '001', 1 FROM dual
)
SELECT * FROM course;
