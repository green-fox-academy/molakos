'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express();

var items = {'completed': false, 'id': 0, 'text': "Pick up the car."},
            {'completed': false, 'id': 1, 'text': "Pick up sister."},
            {'completed': false, 'id': 2, 'text': "Pick up mother."},


app.use(express.static('public'));
app.use(bodyParser.json());

app.get('/todos', function(req, res) {
  res.json(items.all());
});

var newTodo = {'id' = ;
  this.text = '';
}
