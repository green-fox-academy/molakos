"use-strict"

var mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();

var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(id) {
  connection.query('SELECT id, text, status FROM todo WHERE id=?', id, function(err, result) {
    if (err) throw err;
  });
}

function addItem(attributes) {
  // var sql = "INSERT INTO todo SET text= 'hello', status= 'new'";
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function removeItem(id) {
  connection.query('DELETE FROM todo WHERE id=?', id, function(err, result) {
    if (err) throw err;
  });
}

function allItems(cb) {
  connection.query('SELECT * FROM todo', function(err, result) {
    if (err) throw err;
    cb(result);
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};
