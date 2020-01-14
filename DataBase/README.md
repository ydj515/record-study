# DataBase

- **7daySQL Challenge :** https://github.com/ydj515/record-study/tree/master/DataBase/7daySQL

- **DB 멘토링 :** https://github.com/ydj515/record-study/tree/master/DataBase/DB_Mentoring



## Oracle 설치
### Window
1. Oracle Database 12c Release 1 (12.1.0.2.0) - Enterprise Edition
- file 1,2 둘다 설치  
- https://www.oracle.com/database/technologies/oracle-database-software-downloads.html

2. SQL Developer
- https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html

<img width="1404" alt="스크린샷 2020-01-11 오후 1 03 26" src="https://user-images.githubusercontent.com/32935365/72321422-30a9c880-36e7-11ea-8926-5a4b34c6bcdd.png">


### Mac

1. Docker 설치

2. Docker Oracle Database image down
- docker에 설치 하고 싶은 이미지를 docker에서 검색하여 다운로드

```
docker pull store/oracle/database-enterprise:12.2.0.1
```

- 이미지 다운 확인
```
docker images
```

- Oracle 실행  
store/oracle/database-enterprise:12.2.01.의 docker image를 local_db라는 이름으로 프로세스를 실행  
```
docker run -dit --name local_db -p 1521:1521 store/oracle/database-enterprise:12.2.0.1
```

- Docker에서 Oracle 실행 확인
```
docker ps
```
![docker ps](https://user-images.githubusercontent.com/32935365/72321436-3acbc700-36e7-11ea-8508-25e989a770f6.png)  


- 포트 확인
```
lsof -PiTCP -sTCP:LISTEN
```
![포트 listen](https://user-images.githubusercontent.com/32935365/72321451-46b78900-36e7-11ea-9939-47f2ccef895a.png)  


- Docker Oracle 중지
```
docker stop local_db
```

- Docker Oracle 재시작
```
docker restart local_db
```

- SQL Plus 접속  
sys as sysdba로 접속해야함!!
```
docker exec -it local_db bash -c "source /home/oracle/.bashrc; sqlplus sys/Oradoc_db1@ORCLCDB as sysdba"
```
![sql 접속](https://user-images.githubusercontent.com/32935365/72321463-4f0fc400-36e7-11ea-855b-2f1ed8ce6829.png)  





3. SQL Developer
- https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html
- 설정 저장 후 테스트 후 접속
![sql developer 연동](https://user-images.githubusercontent.com/32935365/72321487-5c2cb300-36e7-11ea-8be1-f64dcc256b37.png)  


- Oracle 서버와 연동

## 특이 사항
### Sysdba 임에도 불구하고 create user가 안되는 경우
- Oracle 12c 버전은 명명 규칙이 너무 까다로워서 그럴 때가 있다.
- 해결방법
    1. user 앞에 c##을 붙힌다
    ```
    create c##user aaa indentified by 'aaa'
    ```
    2.  원래 기존 처럼 편하게 생성 가능(이게 베스트)
    ```
    ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;
    ```


[출처]  
https://blog.naver.com/qor3326/220934450444  
https://wookoa.tistory.com/239 [Wookoa]  
https://forgiveall.tistory.com/352 [하하하하하]