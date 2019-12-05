const http = require('http');
const express = require('express')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');

// db connect
var client = require('mysql').createConnection({
    user: 'root',
    password: 'root',
    database: 'location'
});

// create webserver
var app = express();
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});

// /tracker
app.get('/tracker', (req, res) => {
    fs.readFile('Tracker.html', (error, data) => {
        res.send(data.toString());
    });
});

// /observer
app.get('/observer', (req, res) => {
    fs.readFile('Observer.html', (error, data) => {
        res.send(data.toString());
    });
});

// /showdata
app.get('/showdata', (req, res) => {
    // db data 제공
    client.query('SELECT * FROM locations WHERE name=?', [req.param('name')], (error, data) => {
        res.send(data);
    });
});

// create & run socket server
const io = socketio.listen(server);
io.sockets.on('connection', (socket) => {

    // join event
    socket.on('join', (data) => {
        socket.join(data);
    });

    // location event
    socket.on('location', (data) => {
        // insert data
        client.query('INSERT INTO locations(name, latitude, longitude, data) VALUES (?, ?, ?, NOW())', [data.name, data.latitude, data.longitude]);
    
        // receive event emit
        io.sockets.in(data.name).emti('receive', {
            latitude: data.latitude,
            longitude: data.longitude,
            date: Date.now()
        });
    });
});