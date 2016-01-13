'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');


var listCallback = function(response) {
  console.log(JSON.parse(response));
  var todoItems = JSON.parse(response);
  todoItems.forEach(function (todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  });
}

var refresh = function() {
  createRequest('GET', url, {}, listCallback);
}

var newTodo = JSON.stringify({text: 'takaritsunk'});
var createTodoCallback = function(response) {
  refresh();
}

createRequest('POST', url, newTodo, createTodoCallback);
