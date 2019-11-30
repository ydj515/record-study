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

// connect connection event to socket server
// client가 웹 소켓 서버에 접속할 때 발생
io.sockets.on('connection', (socket) => {

    // id 설정
    id = socket.id;

    // aaa라는 소켓 이벤트 연결
    socket.on('aaa',(data) => {
        console.log('Client send data:', data);

        // client에 bbb 이벤트 발생(public 통신: 자신을 포함한 모든 client에게 전달)
        socket.emit('bbb', data);

        // client에 bbb 이벤트 발생(brodcast 통신: 자신을 제외한 모든 client에게 전달)
        // socket.braodcast.emit('bbb', data);

        // client에 bbb 이벤트 발생(private 통신: 특정 id client에게 전달)
        // io.socket.sockets[id].emit('bbb', data);
    });
});