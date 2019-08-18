# Linux-command

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
