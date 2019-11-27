const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const fs = require('fs');
const ejs = require('ejs');
const jade = require('jade');


// const server = http.createServer((req, res) => {
//     res.statusCode = 200;
//     res.setHeader('Content-Type', 'text/plain');
//     res.end('Hello World\n');
// });

// ejsPage.js
// const server = http.createServer((req, res) => {
//     // ejsPage.js 파일 읽기
//     fs.readFile('ejsPage.js','utf8',(error, data) => {
//         res.writeHead(200,{'Content-Type':'text/html'});
//         res.end(ejs.render(data));
//     });
// });

// ejsPage2.js
// const server = http.createServer((req, res) => {
//     // ejsPage.js 파일 읽기
//     fs.readFile('ejsPage2.ejs','utf8',(error, data) => {
//         res.writeHead(200,{'Content-Type':'text/html'});
//         res.end(ejs.render(data, {
//             name: 'RintIanTta',
//             description: 'Hello ejs With Node.js!'
//         }));
//     });
// });

// jadePage.jade
// const server = http.createServer((req, res) => {
//     fs.readFile('jadePage.jade','utf8',(error, data) => {
//         // jade 모듈을 사용
//         var fn = jade.compile(data);

//         res.writeHead(200,{'Content-Type':'text/html'});
//         res.end(fn());
//     });
// });

// jadePage2.jade
const server = http.createServer((req, res) => {
    fs.readFile('jadePage2.jade','utf8',(error, data) => {
        // jade 모듈을 사용
        var fn = jade.compile(data);

        res.writeHead(200,{'Content-Type':'text/html'});
        res.end(fn({
            name: 'RintIanTta',
            description: 'Hello ejs With Node.js!'
        }));
    });
});

server.listen(port, hostname, () => {
    console.log(`server running at http://${hostname}:${port}/`);
});