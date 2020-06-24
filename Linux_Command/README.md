# Linux command

### Tail
- tail -[라인수]f [파일명] : 파일이 바뀌는거 반영해서 계속 모니터링
```
$ tail -200f extract.log
```

### Crontab(예약 실행)
- 예약실행목록 확인
```
$ crontab -l
```
- 예약 실행목록 수정
```
$ crontab -e
$ 0 0 * * * cd /app/ec/migartion_mongodb_thread/migration5 && ./migration.sh start
```
- crontab 시간 예시  
    - ```0 5 * * *``` : 매일 5시 0분에 실행
    - ```5 * * * *``` : 매시 5분이 될 때마다 실행. 즉, 한 시간 간격으로 실행
    - ```* * * * *``` : 1분에 한 번씩 실행
    - ```0 5 1 * *``` : 매달 1일 새벽 5시에 실행
    - ```*/5 * * * *``` : 5분에 한 번씩
    - ```0 */5 * * *``` : 5시간에 한 번씩
    - ```0 5,11 * * *``` : 새벽 5시와 밤 11시
    - ```0 5,11 * * 0,3``` : 매주 일요일과 수요일 새벽 5시와 밤 11시


### bash version 확인
```
$ bash --version
```
### CPU 사용량
```
$ top
```

### 메모리 사용량
```
$ free -mh
$ watch -d -n 0.1 free -mh
```

### 프로세스 검색
```
$ ps -ef | grep <이름>
$ ps -ef | grep python
```

### 데몬(background ps) 상태 확인
```
$ service <데몬이름> status
```

### 네트워크 연결 상태 확인
```
$ ifconfig
```

### 라우팅 테이블
```
$ route
```

### 포트 열려있는지 확인
```
$ nc <호스트명> <포트>
$ nc localhost 8080
```
-호스트명을 외부 server 놓고 nc 명령 치면 차단 되었는지 확인 가능  

### UDP
```
$ nc -u <호스트명> <포트>
```

### 포트 겹치면 누가 사용하고 있는지 확인
```
$ lsof -i TCP:80
$ lsof -c <ps이름>
```

### 서버 응답이 느려졌을 때
```
$ netstat -nap | grep ESTABLISH | wc
$ netstat -nap | grep TIME_WAIT | wc
```
