const http = require('http');
const express = require('express');
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');
const ejs = require('ejs');
const jade = require('jade');

// dummyDB 
var DummyDB = ( () =>{

    // declare variable
    var DummyDB = {};
    var storage = [];
    var count = 1;

    DummyDB.get = (id) => {
        if(id) {
            // process variable
            // id가 string이라면 number 형태로 바꿔줌
            id = (typeof id == 'string') ? Number(id) : id;

            // select data process
            for(var i in storage) if(storage[i].id == id) {
                return storage[i];
            }
            
        } else {
            return storage;
        }
    };

    DummyDB.insert = (data) => {
        data.id = count++;
        storage.push(data);
        
        return data;
    };

    DummyDB.remove = (id) => {

        // process variable
        // id가 string이라면 number 형태로 바꿔줌
        id = (typeof id == 'string') ? Number(id) : id;

        // delete data process
        for(var i in storage) if(storage[i].id == id) {
            storage.splice(i, 1);

            return true; // delete success
        }

        return false; // delete fail
    };

    return DummyDB;
})();

// create server
var app = express();

// set middle ware
// app.use(express.logger());
app.use(express.cookieParser())
app.use(express.bodyParser())
app.use(app.router());

// set router
app.get('/user',(req, res) => {
    res.send(DummyDB.get());
});

app.get('/user/:id',(req, res) => {
    res.send(DummyDB.get(req.param('id')));
});

app.post('/user',(req, res)=>{

    // declare variable
    var name = req.param('name');
    var region = req.param('region');

    // valid check
    if(name && region) {
        res.send(DummyDB.insert({
            name: name,
            region: region
        }));
    } else {
        throw new Error('insert error');
    }
});

app.put('/user/:id',(req, res) => {
    
    // delcare variable
    var id = req.param('id');
    var name = req.param('name');
    var region = req.param('region');

    // modify DB
    var item = DummyDB.get(id);
    item.name = name || item.name;
    item.region = region || item.region;

    res.send(item);
});

app.del('/user/:id',(req, res) => {
    res.send(DummyDB.remove(req.param('id')));
});

// run server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});