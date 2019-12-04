const http = require('http');
const socketio = require('socket.io');
const express = require('express')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');

var seat = [
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,0,0,0,0,1,1,0,1,1],
]

var app = express();

// router
app.use(app.router);

app.get('/',(req, res, next) => {
    fs.readFile('HTMLPage.html',(error, data) => {
        res.send(data.toString());
    });
});

app.get('/seats',(req, res, next) => {
    res.send(seats);
});

// start server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});

// create & run socket server
const io = socketio.listen(server);
io.sockets.on('connection', (socket) => {
    socket.on('reserve', (data) => {
        seats[data.y][data.x] = 2; // 예약된 상태는 2로 바꿈
        io.sockets.emit('reserve', data);
    });
});