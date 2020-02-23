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

## Request Parameter
- ejs와 js의 request parameter 주고 받는 법
- js file

```js
router.get('/', function(req, res, next) {

    console.log(req.query.name); // 아래 ejs 파일에서 /issuedetail?name= 값을 넘겨 받는다

    mysqlDB.query('SELECT * FROM article a WHERE a.sub_cat_id IN( SELECT cat_id FROM category WHERE name=' + "'" + req.query.name + "') ORDER BY a.article_id DESC", function (err, rows, fields) {
        if (!err) {
            console.log(rows);
            // console.log(fields);
            res.render('issuedetail', { mylist: rows });
        } else {
            console.log('query error : ' + err);
            res.send(err);
        }
    });
});
```

- ejs file
```html
<tbody style="overflow-y: auto; overflow-x: hidden; float: left;height:70vh">
  <tr>
    <td colspan="3"><%=mylist.length%></a></td>
  </tr>
  <% for ( var i = 0; i < mylist.length; i++){ %>
  <tr>
    <td colspan="3"><a href="/issuedetail?name=<%=mylist[i].name%>"><%=mylist[i].name%></a></td>
  </tr>
  <% } %>
</tbody>
```

## Supervisor
- **Node js를 자동으로 재시작**
```
npm install supervisor -g
```

## Node 버전 관리(업데이트 및 다운그레이드)

### Node 버전 확인
```
node -v
```

### node cache 삭제
- Node.js 의 패키지매니저인 npm 을 이용하여 대부분의 플러그인을 설치할 때 캐시가 남아있는 경우 에러가 날 수 있음
- 캐시를 미리 삭제
```
sudo npm cache clean -f
```

### n 모듈 설치
```
sudo npm install -g n
```

### Node 버전 설치
- 최신버전 설치
```
n latest
```
- Stable버전 설치
```
n stable
```
- LTS버전 설치
```
n lts
```

- 특정 버전 설치
```
n 12.13.1
n 0.8.14
n 0.8.17
n 0.9.6
```

### 버전 변경하기
- 화살표로 움직이면서 버전 변경 가능
```
n
```

### 현재 버전 외에 모든 버전 삭제
```
n prune
```

### npm 재설치
```
npm -V
sudo npm install -g npm
npm -V
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

## Datetime Formatting
- ejs에서 사용하기 위해 DB안에 있는 Date형식을 원하는 방식대로 format

### moment 모듈 설치
```
npm install moment
npm install
```

### moment 모듈 사용
- 해당 js 파일에 모듈 사용
```js
var moment = require('moment'); // npm install moment : 날짜 포맷 변경
```

- rendering 하는 부분에 moment를 붙혀서 넘겨줌
```js
res.render('ddetail', { mylist: rows, name: req.query.name, moment});
```

- 해당 ejs 에서 사용
```html
<%=moment(mylist[mylist.length-1].reg_date).format('YYYY.MM.DD') %>
```

## DB관련 에러
### {"code":"PROTOCOL_ENQUEUE_AFTER_FATAL_ERROR","fatal":false} DB 커넥션 에러
- DB 커넥션. 즉, DB 요청이 없어서 timeout 현상발생하는 에러
- 의미없는 쿼리를 지속적으로 보내주어 연결을 유지시킴
- app.js
```js
setInterval( () => {
  mysqlDB.query('SELECT 1');
}, 5000);

```

## node 와 vue 연동
- 기존 esj에서 vue로 front를 바꾼다.
- ejs파일들이 있는 views 폴더를 기반으로 작업

### vue 및 express-vue 모듈 설치
```
npm install vue -g
npm install vue-cli -g
npm install --save express-vue
npm install
```

### express-vue 세팅
- app.js
```js
var expressVue = require('express-vue');

const vueOptions = {
  VUE_DEV: true,
  rootPath: path.join(__dirname, '/views') // 폴더 경로를 잘 맞춰준다
};
const expressVueMiddleware = expressVue.init(vueOptions);

var app = express();
app.use(expressVueMiddleware);
```

- index.js
```js
res.renderVue('index.vue',{ mylist: rows });
```

- index.vue
``` vue
<template>
    <div>
        <h1>{{mylist}}</h1>
        <table>
            <thead>
            </thead>
        <tbody>
            <tr v-for="result in mylist" v-bind:key="result">
                <td>{{result.name}}</td>
                <td>{{result.cat_id}}</td>
            </tr>
        </tbody>
    </table>
    </div>

</template>

<script>
    module.exports = {
        data: function () {
            return {
                title: '',

            }
        },
    }
</script>
```
