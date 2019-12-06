const http = require('http');
const socketio = require('socket.io');
const express = require('express')
const ejs = require('ejs')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');

var app = express();
var counter = 0;

function Product(name, image, price, count) {
    this.index = counter++;
    this.name = name;
    this.image = image;
    this.price = price;
    this.count = count;
}

var products = [
    new Product('JavaScript', 'chrome.png', 28000, 30),
    new Product('jQuery', 'chrome.png', 28000, 30),
    new Product('Node.js', 'chrome.png', 32000, 30),
    new Product('Socket.io', 'chrome.png', 17000, 30),
    new Product('Connect', 'chrome.png', 18000, 30),
    new Product('Express', 'chrome.png', 31000, 30),
    new Product('EJS', 'chrome.png', 12000, 30),
]

// routing
app.use(app.router);
app.use(express.static(__dirname + '/public'));

app.get('/',(req, res) => {
    var HTMLPage = fs.readFileSync('HTMLPage.html', 'utf8');

    res.send(ejs.render(HTMLPage, {
        products: products
    }));
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

    function onReturn(index) {
        products[index].count++; // 물건 개수를 증가
       
        clearTimeout(cart[index].timerID); // 타이머를 제거
        
        delete cart[index]; // 카트에서 물건을 제거
        
        io.sockets.emit('count', {
            index: index,
            count: products[index].count
        });
    };

    var cart = {};
    // cart event
    socket.on('cart', (index) => {
        products[index].count--; // 물건의 개수 감소

        cart[index].index = index; // 카트에 물건을 넣고 타이머를 시작
        cart[index].timerID = setTimeout( () => {
            onReturn(index);
        }, 1000*60*10);

        // count event
        io.sockets.emit('count', {
            index: index,
            count: products[index].count
        });
    });

    // buy event
    socket.on('buy', (index) => {
        clearTimeout(cart[index].timerID); // 타이머를 제거
        
        delete cart[index]; // 카트에서 물건을 제거
        
        io.sockets.emit('count', {
            index: index,
            count: products[index].count
        });
    });

    // return event
    socket.on('return', (index) => {
        onReturn(index);
    });

});