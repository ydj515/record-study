const http = require('http');
const socketio = require('socket.io');

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');

const server = http.createServer((req, res) => {
    fs.readFile('htmlPage.html','utf8',(error, data) => {
        res.writeHead(200,{'Content-Type':'text/html'});
        res.end(data)
    });
});

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});

// create & run socket server
const io = socketio.listen(server);

// 특정 client를 구분하기 위한 id
var id = 0;

var globalVariable = {};

// connect connection event to socket server
// client가 웹 소켓 서버에 접속할 때 발생
io.sockets.on('connection', (socket) => {

    // setname 이벤트 발생할 때
    socket.on('setname', (data) => {
        socket.name = data; // socket session에 저장
        console.log('data: ', socket.name);
    });

    socket.on('getname', () => {
        socket.emit('responsename', socket.name);
        console.log('data: ', socket.name);
    });
});