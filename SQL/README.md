# SQL

- <a href="https://programmers.co.kr/events/7day-sql?utm_source=programmers&utm_medium=learn_7daySQL&utm_campaign=7daySQL">7daySQL 챌린지</a>

## Table 설명
![ins](https://user-images.githubusercontent.com/32935365/64474671-04b78d00-d1b3-11e9-87a6-4384461710dd.PNG)
![outs](https://user-images.githubusercontent.com/32935365/64474678-15680300-d1b3-11e9-8c7e-2bbd9a08b42b.PNG)


## Table 내용
![2](https://user-images.githubusercontent.com/32935365/64315628-8a89db80-cfed-11e9-920f-5ba5c08808aa.PNG)

<hr>

### DAY 1-1

#### 문제
![1](https://user-images.githubusercontent.com/32935365/64316314-6b8c4900-cfef-11e9-969b-e17d1c35db4e.PNG)
#### 답
```SQL
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### DAY 1-2

#### 문제
![2](https://user-images.githubusercontent.com/32935365/64316484-ed7c7200-cfef-11e9-8010-bfd69b168847.PNG)
#### 답
```SQL
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```

### DAY 2-1

#### 문제
![3](https://user-images.githubusercontent.com/32935365/64316615-4c41eb80-cff0-11e9-9d88-e37f46aa4948.PNG)
#### 답
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION="Sick"
ORDER BY ANIMAL_ID
```

### DAY 2-2

#### 문제
![4](https://user-images.githubusercontent.com/32935365/64316630-5663ea00-cff0-11e9-88e7-a778723c90db.PNG)
#### 답
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION="Aged"
ORDER BY ANIMAL_ID
```

### DAY 3-1

#### 문제
![5](https://user-images.githubusercontent.com/32935365/64316774-cbcfba80-cff0-11e9-8881-d5d2b82fea73.PNG)
#### 답
```SQL
SELECT MIN(DATETIME)
FROM ANIMAL_INS
```

### DAY 3-2

#### 문제
![6](https://user-images.githubusercontent.com/32935365/64316782-d2f6c880-cff0-11e9-9d41-8ed4353e89a8.PNG)
#### 답
```SQL
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is NULL
```

### DAY 4-1

#### 문제
![7](https://user-images.githubusercontent.com/32935365/64316914-2701ad00-cff1-11e9-9039-bebb2772e464.PNG)
#### 답
```SQL
SELECT ANIMAL_TYPE, count(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
```

### DAY 4-2

#### 문제
![8](https://user-images.githubusercontent.com/32935365/64316921-3123ab80-cff1-11e9-9653-ab9d155c9213.PNG)
#### 답
```SQL
SELECT NAME, count(*)
FROM ANIMAL_INS
Where NAME is NOT NULL
GROUP BY NAME
HAVING COUNT(*)>=2 ORDER BY NAME
```

### DAY 5-1

#### 문제
![9](https://user-images.githubusercontent.com/32935365/64474686-27e23c80-d1b3-11e9-984a-5260ea0b22f0.PNG)
#### 답
```SQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_OUTS AS B
WHERE NOT B.ANIMAL_ID IN (SELECT ANIMAL_ID FROM ANIMAL_INS)
```

### DAY 5-2

#### 문제
![10](https://user-images.githubusercontent.com/32935365/64474688-30d30e00-d1b3-11e9-9c10-06babfc49d60.PNG)
#### 답
```SQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE B.DATETIME < A.DATETIME
ORDER BY A.DATETIME ASC
```

### DAY 6-1

#### 문제
![11](https://user-images.githubusercontent.com/32935365/64474699-45afa180-d1b3-11e9-9ab5-c804c59aea2a.PNG)
#### 답
```SQL
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.DATETIME is NULL
ORDER BY A.DATETIME ASC
LIMIT 3
```

### DAY 6-2

#### 문제
![12](https://user-images.githubusercontent.com/32935365/64474703-4b0cec00-d1b3-11e9-88bb-2b4b91f5380b.PNG)
#### 답
- Spayed 와 Neutered이 중성화를 의미한다!!
```SQL
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME 
FROM ANIMAL_OUTS AS A
JOIN ANIMAL_INS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID 
WHERE B.SEX_UPON_INTAKE LIKE 'Intact%' 
AND (A.SEX_UPON_OUTCOME LIKE 'Spayed%' OR A.SEX_UPON_OUTCOME LIKE 'Neutered%') 
ORDER BY A.ANIMAL_ID;
```

### DAY 7-1

#### 문제
![13](https://user-images.githubusercontent.com/32935365/64477360-ad76e400-d1d5-11e9-98d0-4309baef4b25.PNG)
#### 답
```SQL
SELECT DISTINCT ANIMAL_ID,NAME,SEX_UPON_INTAKE 
FROM ANIMAL_INS 
WHERE NAME='Lucy' or NAME='Ella' or NAME='Pickle' or NAME='Rogan' or NAME='Sabrina' or NAME='Mitty'
ORDER BY ANIMAL_ID;
```

### DAY 7-2

#### 문제
![14](https://user-images.githubusercontent.com/32935365/64477354-8f10e880-d1d5-11e9-9278-e1d54bd126ec.PNG)
#### 답
- Spayed 와 Neutered이 중성화를 의미한다!!
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE="Dog" and UPPER(NAME) like UPPER("%el%")
ORDER BY NAME ASC
```
