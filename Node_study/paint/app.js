const http = require('http');
const socketio = require('socket.io');
const express = require('express')
const ejs = require('ejs')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');

var app = express();

// router
app.use(app.router);
app.use(express.static('public'))

app.get('/', (req, res) => {
    fs.readFile('lobby.html', (error, data) => {
        res.send(data.toString());
    });
});

app.get('/canvas/:room', (req, res) => {
    fs.readFile('canvas.html', 'utf8', (error, data) => {
        res.send(ejs.render(data, {
            room: req.param('room')
        }));
    });
});

app.get('room/', (req, res) => {
    fs.readFile('lobby.html', (error, data) => {
        res.send(io.sockets.manager.rooms);
    });
});

// start server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});

// create & run socket server
const io = socketio.listen(server);
io.set('log level', 2)
io.sockets.on('connection', (socket) => {
    
    socket.on('join', (data) => {
        socket.join(data);
        socket.set('room',data);
    });
   
    socket.on('draw', (data) => {
        socket.get('room',(error, room) => {
            io.sockets.in(room).emit('line',data);
        });
    });
    
    socket.on('create_room', (data) => {
        io.sockets.emit('create_room', data.toString());
    });


});