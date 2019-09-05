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
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID
```

### DAY 1-2

#### 문제
![2](https://user-images.githubusercontent.com/32935365/64316484-ed7c7200-cfef-11e9-8010-bfd69b168847.PNG)
#### 답
```SQL
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC
```

### DAY 2-1

#### 문제
![3](https://user-images.githubusercontent.com/32935365/64316615-4c41eb80-cff0-11e9-9d88-e37f46aa4948.PNG)
#### 답
```SQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION="Sick" ORDER BY ANIMAL_ID
```

### DAY 2-2

#### 문제
![4](https://user-images.githubusercontent.com/32935365/64316630-5663ea00-cff0-11e9-88e7-a778723c90db.PNG)
#### 답
```SQL
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NOT INTAKE_CONDITION="Aged" ORDER BY ANIMAL_ID
```

### DAY 3-1

#### 문제
![5](https://user-images.githubusercontent.com/32935365/64316774-cbcfba80-cff0-11e9-8881-d5d2b82fea73.PNG)
#### 답
```SQL
SELECT MIN(DATETIME) FROM ANIMAL_INS
```

### DAY 3-2

#### 문제
![6](https://user-images.githubusercontent.com/32935365/64316782-d2f6c880-cff0-11e9-9d41-8ed4353e89a8.PNG)
#### 답
```SQL
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME is NULL
```
