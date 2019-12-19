# Node.js-study

## What is Node.js
### javascript engine(V8 Engin)에 기반해 만들어진 server side platform
### 비동기 I/O 처리
- readFile은 비동기. readFileSync는 동기.
```js
// Blocking Code
const fs = require('fs');
const data = fs.readFileSync('/file.md'); // 파일을 읽을 때까지 여기서 블로킹 됩니다.
console.log(data);
```

```js
// Noe Blocking Code
const fs = require('fs');
fs.readFile('/file.md', (err, data) => {
    if (err) throw err;
    console.log(data);
});
```

### 이벤트 처리 위주
- 이벤트 감지기 Callback 함수 호출
- 이벤트를 대기하는 Main loop 존재
- event handling은 **Observer pattern**
![event](https://user-images.githubusercontent.com/32935365/69825899-3f7e0e00-1254-11ea-9bf5-ba3908782efb.PNG)  

```js
// events 모듈 사용
var events = require('events');

// EventEmitter 객체 생성
var eventEmitter = new events.EventEmitter();

// EventHandler 함수 생성
var connectHandler = function connected(){
    console.log("Connection Successful");
    
    // data_recevied 이벤트를 발생시키기
    eventEmitter.emit("data_received");
}

// connection 이벤트와 connectHandler 이벤트 핸들러를 연동
eventEmitter.on('connection', connectHandler);

// data_received 이벤트와 익명 함수와 연동
// 함수를 변수안에 담는 대신에, .on() 메소드의 인자로 직접 함수를 전달
eventEmitter.on('data_received', function(){
    console.log("Data Received");
});

// connection 이벤트 발생시키기
eventEmitter.emit('connection');

console.log("Program has ended");
```


### 빠른 속도
- 동시성으로 빠른 작업 가능

### single thread

### No Buffering

## Node.js를 사용하면 좋은 분야
- 입출력이 많은 App
- data String App
- data를 실시간으로 다루는 App
- JSON API 기반 App
- Single Page App

##  Node.js를 사용하면 않좋은 분야
- CPU 사용량이 높은 App

## Node.js 시작
### donwload Node.js
 - https://nodejs.org/ko/
  
### npm donwload
- -g 옵션은 global 옵션
```
npm install install npm -g
```

### 모듈 설치
```
npm install {모듈 이름} -g
npm install express -g
```

### 모듈 제거
```
npm uninstall {모듈 이름}
npm uninstall express
```

### 모듈 업데이트
```
npm update {모듈 이름}
npm update express
```

### 모듈 검색
```
npm search {모듈 이름}
npm search express
```

### package.josn
- 노드 어플리케이션, 모듈의 경로에 있으며 패키지 속성을 정의
```json
{
  "name": "ejs-sample",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "node ./bin/www"
  },
  "dependencies": {
    "cookie-parser": "~1.4.4",
    "debug": "~2.6.9",
    "ejs": "~2.6.1",
    "express": "~4.16.1",
    "http-errors": "~1.6.3",
    "morgan": "~1.9.1"
  }
}
```

## Http server
```js
const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});
```


## Express 사용


## Supervisor
- **Node js를 자동으로 재시작**
```
npm install supervisor -g
```


## Memroy Leak
![js_out_of_memory](https://user-images.githubusercontent.com/32935365/71154077-0e569380-227e-11ea-93f4-b8e420879fba.PNG)  

### 메모리 누수 원인
- node js는 v8엔진에서 **GC(Garbage Collector)를 주기적으로 수행**
- node js는 **메모리 관리가 불완전하고 어렵다.** 왜냐하면 GC(Garbage Collector)역시 **메인스레드(이벤트루프)에서 실행되기 때문**
- 따라서 메인스레드가 바쁜 작업(CPU인텐시브)을 돌릴 경우, 메모리는 급격히 증가하여 Memory Allocate Error 발생

### 해결 방안
- 1. **process.nextTick과 setTimeout**을 활용하여 GC가 수행될 수 있도록 시간틈을 만들어주는 법
- 2. **closer와 stack의 빈번한 사용을 자제**
- 3. **GC를 수동으로 event loop에 넣음**(일시적인 블록이 발생할 수 있어 성능이 저하된다는 단점)

### heap memory 사이즈 늘리기
기본적인 nodejs의 할당된 메모리양은 512MB  

- 일반적인 경우(4GB로 늘림)
```
node --max-old-space-size=4096 app.js
```

- webpack 사용하는 경우(4GB로 늘림)
```
webpack --config webpack.build.config.js --max_old_space_size=4096
```
