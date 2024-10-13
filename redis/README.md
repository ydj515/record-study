# Redis
NoSQL DB로 key-value로 저장되며 지원 되는 데이터 타입(string, hash, list, set, zset, bitmap ...)이 여러개 존재 <br/>

메모리 내에서 작동하며, 디스크에 데이터를 저장하거나 로딩도 가능 <br/>
캐싱, 세션 관리, 메시지 브로커 등으로 사용 <br/>



### install(centos 8)

#### repository install
```sh
$ sudo dnf install epel-release
```

#### redis install
```sh
$ sudo dnf install redis
```

#### service 등록 및 start
```sh
$ sudo systemctl enable redis
$ sudo systemctl start redis
```

#### redis-console
```sh
$ redis-cli
```

#### redis 정상작동 확인
ping 명령어를 날리면 pong으로 날라온다.
```sh
$ redis-cli
> ping
    - pong
```


### redis 문법
key-value 구조로 가지고 있고 value에는 string, hash, list, set, zset, bitmap등이 올 수 있다.

#### string
```
set mykey " 
```