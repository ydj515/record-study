# SQL

- <a href="https://github.com/ydj515/Algorithm_study/blob/master/Java/src/num15953/Main.java">7daySQL 챌린지</a>

## Table 설명
![1](https://user-images.githubusercontent.com/32935365/64315607-7cd45600-cfed-11e9-83ee-f78d1c0c8aba.PNG)

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
![9](https://user-images.githubusercontent.com/32935365/64366382-108b3e00-d051-11e9-82fa-ad8c7d3fb8c0.PNG)
#### 답
```SQL
SELECT b.ANIMAL_ID, b.NAME
from ANIMAL_OUTS b
WHERE NOT b.ANIMAL_ID IN (SELECT ANIMAL_ID FROM ANIMAL_INS)
```

### DAY 5-2

#### 문제
![10](https://user-images.githubusercontent.com/32935365/64366401-1a14a600-d051-11e9-80bc-b7a8f5b80874.PNG)
#### 답
```SQL
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.ANIMAL_ID=B.ANIMAL_ID WHERE B.DATETIME < A.DATETIME
order by A.DATETIME ASC
```
