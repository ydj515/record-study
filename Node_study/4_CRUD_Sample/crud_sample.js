const http = require('http');
const express = require('express');
const mysql = require('mysql');
const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');
const ejs = require('ejs');

// connect database
var client = mysql.createConnection({
    user: 'root',
    password: 'root',
    database: 'Company'
});

// create server
var app = express();

// set middle ware
app.use(app.router)

// set router
app.get('/',(req, res) =>{
    // read file
    fs.readFile('list.html','utf8',(error, data) => {
        //execute query
        client.query('SELECT * FROM products', (error, results) => {
            res.send(ejs.render(data, {
                data: results
            }));
        });
    });
});

app.get('/delete/:id',(req, res) =>{
    // execute query
    client.query('DELETE FROM products WHERE id=?', [req.param('id')], () => {
        res.redirect('/');
    });
});

app.get('/insert',(req, res) =>{
    // read file
    fs.readFile('insert.html','utf8',(error, data) => {
        res.send(data)
    });
});

app.post('/insert',(req, res) =>{
    // declare variable
    var body = req.body;

    // execute query
    client.query('INSERT INTO products (name, modelnumber, series) VALUES (?, ?, ?)', [
        body.name, body.modelnumber, body.series
    ], () => {
        res.redirect('/');
    });
});

app.get('/edit/:id',(req, res) =>{
    // read file
    fs.readFile('edit.html','utf8',(error, data) => {
        // execute query
        client.query('SELECT * FROM products WHERE id = ?', [
            req.params,('id')
        ], (error, result) => {
            res.send(ejs.render(data, {
                data: result[0]
            }));
        });
    });
});

app.post('/edit:id',(req, res) =>{
    // declare variable
    var body = req.body

    // execute query
    client.query('UPDATE products SET name=?, modelnumber=?, series=? WHERE id=?', [
        body.name, body.modelnumber, body.series, req.param('id')
    ], () => {
        res.redirect('/');
    });
});

// run server
const server = http.createServer(app);

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});