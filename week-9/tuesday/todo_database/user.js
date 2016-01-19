'use strict';

var mysql = require('mysql');

var connection = mysql.createConnection({
  host : 'localhost',
  user : 'test',
  password : 'test',
  database : 'todo'
});

connection.connect();

function addUser(attributes) {
  var sql = "INSERT INTO todo SET text= 'hello', status= 'new'";
  connection.query('INSERT INTO user SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

function getUserById(attributes, cb) {
  connection.query(
    "SELECT * FROM 'user' WHERE user_id=?", [attributes.user_id],
    function(err, results) {
      if(err) throw err;
      console.log();
    }
  )
}

module.exports = {
  add: addUser,
  // get: getUser,
  // getUserById: getUserById
};
