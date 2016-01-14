'use strict';

var express = require('express');
var url = require('url');
var app = express();
var bodyParser = require('body-parser')

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}))

app.get('/', function(req, res) {
  res.send('Hello world!');
});

app.get('/add', function(req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;

  var a = parseInt(query['a']);
  var b = parseInt(query['b']);
  var result = a + b;

  res.send(result.toString() + '\n');
});

app.post('/add', function(req, res) {
  console.log(req.body);
  var a = req.body['a'];
  var b = req.body['b'];
  var result = a + b;
  res.send(result.toString() + '\n')
  // res.status(204).end();
});

app.get('/:name', function (req, res) {
  var name = req.params['name'];
  console.log('name:' + name);
  res.send('Hello, ' + name + '\n');
});

app.listen(3000);
