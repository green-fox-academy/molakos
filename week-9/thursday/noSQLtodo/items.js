"use-strict"

var mongoClient = require('./mongo.js').mongoClient;
var ObjectId = require('ObjectId');
var collectionName = 'todos';

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

function getItem(id, callback) {
  mongoClient(function(err, db) {
    if (err) throw err;

    db.collection(collectionName)
      .find({_id: new ObjectId(id)})
      .limit(1)
      .next(err, docs) {
        if (err) throw err;
        callback(docs);
        db.close();
      });
  });
}

function addItem(attributes) {
  var item = new TodoItem();
  item.update(attributes);

  mangoClient
    db.collection(collectionName)

  return item;
}

function removeItem(id) {
  delete items[id];
}

function allItems(callback) {
  var values = [];

  mongoClient(function(err, db) {
    if (err) throw err;

    db.collection(collectionName)
      .find({})
      .toArray(function(err, docs) {
        if (err) throw err;
        callback(docs);
        db.close();
      });
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};
