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
- Node js에서 사용하는 **FrameWork**
- Java에서 Spring을 주로 사용하듯이 Node 에서는 Express를 사용

### 사용
- ejs사용
```
express -e {dir_name}
```

### Middle ware
- 경로를 마운트 하고 해당 경로로 들어올 경우 실행
- 경로 지정이 안되어 있으므로 모든 경로에 바인드
```js
var app = express();

app.use(function (req, res, next) {
  console.log('Time:', Date.now());
  next();
});
```

- /user/:id 경로
```js
app.use('/user/:id', function (req, res, next) {
  console.log('Request Type:', req.method);
  next(); // next로 미들웨어 함수 표시
});
```
```js
app.get('/user/:id', function (req, res, next) {
  res.send('USER');
});
```

- 라우터 레벨 미들웨어
```js
var app = express();
```

```js
var app = express();
var router = express.Router();

// a middleware function with no mount path. This code is executed for every request to the router
router.use(function (req, res, next) {
  console.log('Time:', Date.now());
  next();
});

// a middleware sub-stack shows request info for any type of HTTP request to the /user/:id path
router.use('/user/:id', function(req, res, next) {
  console.log('Request URL:', req.originalUrl);
  next();
}, function (req, res, next) {
  console.log('Request Type:', req.method);
  next();
});

// a middleware sub-stack that handles GET requests to the /user/:id path
router.get('/user/:id', function (req, res, next) {
  // if the user ID is 0, skip to the next router
  if (req.params.id == 0) next('route');
  // otherwise pass control to the next middleware function in this stack
  else next(); //
}, function (req, res, next) {
  // render a regular page
  res.render('regular');
});

// handler for the /user/:id path, which renders a special page
router.get('/user/:id', function (req, res, next) {
  console.log(req.params.id);
  res.render('special');
});

// mount the router on the app
app.use('/', router);
```

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
