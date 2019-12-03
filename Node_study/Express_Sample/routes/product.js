var express = require('express');
var router = express.Router();

/* GET /product */
// product처럼 폴더를 지정하면 자동으로 product/index.jade를 호출
router.get('/', function(req, res) {
  res.render('product', { title: 'Product Page' });
});

/* GET /product */
router.get('/insert', function(req, res) {
  res.render('product/insert', { title: 'Insert Page' });
});

/* GET /product */
router.get('/edit', function(req, res) {
  res.render('product/edit', { title: 'Edit Page' });
});

module.exports = router;
