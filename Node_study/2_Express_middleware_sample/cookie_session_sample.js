const http = require('http');
const express = require('express');
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');
const ejs = require('ejs');
const jade = require('jade');

// create server
var app = express();

// app.use(express.logger());
app.use(express.cookieParser())
app.use(express.bodyParser())
app.use(app.router());
app.use(app.session({
    secret: 'secret key',
    key: 'init',
    cookie: {
        maxAge: 60 * 1000
    }
}));

// set router
app.get('/',(req, res) =>{
    var output = {};
    

    if(req.cookies.auth) {
        
        output.cookies = req.cookies;
        output.session = req.session;
        
        // save session
        req.session.now = (new Date()).toUTCString();
        
        res.send('<h1>login success</h1>' + '<p>' + output + '</p>');
    } else {
        res.redirect('/login');
    }
});

app.get('/login',(req, res) =>{
    fs.readFile('login.html', (error, data) => {
        res.send(data.toString());
    })
});

app.post('/login',(req, res) =>{
    var id = req.param('login');
    var pw = req.param('password');

    console.log(id, password);
    console.log(req.body);

    if(id=='dongjin' && pw == 'ehdwls515') {
        res.cookie('auth', true); // set cookie name
        res.redirect('/');
    } else {
        res.redirect('/login');
    }
});


// run server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});