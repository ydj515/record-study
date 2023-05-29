# Linux command

### Tail
- tail -[라인수]f [파일명] : 파일이 바뀌는거 반영해서 계속 모니터링
```sh
$ tail -200f extract.log
```

### Crontab(예약 실행)
- 예약실행목록 확인
```sh
$ crontab -l
```
- 예약 실행목록 수정
```sh
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
```sh
$ bash --version
```
### CPU 사용량
```sh
$ top
```

### 메모리 사용량
```sh
$ free -mh
$ watch -d -n 0.1 free -mh
```

### 프로세스 검색
```sh
$ ps -ef | grep <이름>
$ ps -ef | grep python
```

### 데몬(background ps) 상태 확인
```sh
$ service <데몬이름> status
```

### 네트워크 연결 상태 확인
```sh
$ ifconfig
```

### 라우팅 테이블
```sh
$ route
```

### 포트 열려있는지 확인
```sh
$ nc <호스트명> <포트>
$ nc localhost 8080
```
-호스트명을 외부 server 놓고 nc 명령 치면 차단 되었는지 확인 가능  

### UDP
```sh
$ nc -u <호스트명> <포트>
```

### 포트 겹치면 누가 사용하고 있는지 확인
```sh
$ lsof -i TCP:80
$ lsof -c <ps이름>
```

### 서버 응답이 느려졌을 때
```sh
$ netstat -nap | grep ESTABLISH | wc
$ netstat -nap | grep TIME_WAIT | wc
```

### tcpdump
- 네트워크카드를 통해 송수신 되는 패킷을 가로채고 표시해주는 소프트웨어
- option
```
-i : 네트워크 인터페이스가 여러 개일 경우 지정
-c : 스니핑 할 패킷의 개수
-v : 패킷 헤더의 정보를 조금 더 자세하게 보여줌 -vv 하나 더 붙이면 더욱 자세
-n : 알려진 도메인 문자열을 IP 로 보여줌. -nn 하나 더 붙이면 Port 도 숫자로 표시
-w : 스니핑 한 패킷을 .pcap 타입 바이너리로 저장. -r 옵션으로 TXT 타입으로 로드
-A : ASCII로 패킷 내용을 출력. 이는 패킷의 페이로드를 가독성있게 확인
-l : 버퍼를 사용하지 않고 즉시 출력. 실시간으로 패킷을 모니터링하는 용도로 사용
```


- 1024 byte로 패킷 크기를 제한하여 버퍼를 사용하지 않고 즉시 출력
```sh
$ tcpdump -vvvs 1024 -l -A host 3.38.110.138
```
- 인터페이스 eth0 을 보여줌
```sh
$ tcpdump -i eth0 
```
- 결과를 파일로 저장, txt 가 아닌 bin 형식으로 저장됨
```sh
$ tcpdump -w tcpdump.log 
```
- 저장한 파일을 읽음
```sh
$ tcpdump -r tcpdump.log 
```
- 카운터 10개만 보여줌
```sh
$ tcpdump -i eth0 -c 10 
```
- tcp 80 포트로 통신하는 패킷 보여줌
```sh
$ tcpdump -i eth0 tcp port 80 
```
- source ip 가 192.168.0.1인 패킷 보여줌
```sh
$ tcpdump -i eth0 src 192.168.0.1 
```
- destination ip 가 192.168.0.1인 패킷 보여줌
```sh
$ tcpdump -i eth0 dst 192.168.0.1 
```
- dest ip 가 192.168.0.1인 패킷 보여줌
```sh
$ tcpdump -i eth0 dst 192.168.0.1 
```
- host 를 지정하면, 이 ip 로 들어오거가 나가는 양방향 패킷 모두 보여줌
```sh
$ tcpdump host 192.168.0.1 
```
- host 중에서 src 가 192.168.0.1인것 만 지정
```sh
$ tcpdump src 192.168.0.1 
```
- host 중에서 dst 가 192.168.0.1인것 만 지정
```sh
$ tcpdump dst 192.168.0.1 
```
- CIDR 포맷으로 지정할 수 있다.
```sh
$ tcpdump net 192.168.0.1/24 
```
- TCP 인것만
```sh
$ tcpdump tcp 
```
- UDP 인것만
```sh
$ tcpdump udp 
```
- 포트 양뱡항으로 3389인 것.
```sh
$ tcpdump port 3389 
```
- src 포트가 3389인 것.
```sh
$ tcpdump src port 3389 
```
- dst 포트가 3389인 것.
```sh
$ tcpdump dst port 3389 
```
* and 옵션으로 여러가지 조건의 조합 가능
- source ip 가 192.168.0.1이면서 tcp port 80 인 패킷 보여줌
```sh
$ tcpdump -i eth0 src 192.168.0.1 and tcp port 80 
```
- 목적이 ip가 xxx.xx.xx.xx인 곳으로 514포트를 사용하는 udp 패킷을 tcpdump.log 파일에 저장(!)
```sh
$ tcpdump -w tcpdump.log -i eth0 dst xxx.xx.xx.xx and udp and port 514 
```
* combine : and ( &amp;&amp; ) , or ( || ) , not ( ! ) 으로 여러가지를 조합해서 사용 가능
- UDP 이고 src 포트가 53 인 것
```sh
$ tcpdump udp and src port 53 
```
- src ip 가 x.x.x.x 이고 dst 포트가 22 가 아닌 것
```sh
$ tcpdump src x.x.x.x and not dst port 22 
```
* grouping : ( )
- src ip 가 x.x.x.x 이고 ( dst 포트가 3389 또는 22 ) 인 것 ==> 여기서는 ‘ ’ 가 반드시 있어야 한다.
```sh
$ tcpdump ‘src x.x.x.x and ( dst port 3389 or 22 )’
```

### log rotate
