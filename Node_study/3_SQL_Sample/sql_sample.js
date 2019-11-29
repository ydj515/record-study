const http = require('http');
const express = require('express');
const mysql = require('mysql')

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');
const ejs = require('ejs');
const jade = require('jade');

var client = mysql.createConnection({
    user: 'root',
    password: 'root'
});

client.query('USE Company');
client.query('SELECT * FROM products', (error, result, fields) => {
    if(error) {
        console.log('query has error');
    } else {
        console.log(result);
    }
});

// run server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});