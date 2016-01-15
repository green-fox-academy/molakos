'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
var todoContainer = document.querySelector('.todo-container');


var listCallback = function(response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function (todoItem) {
    var newTodoItem = document.createElement('div');
    newTodoItem.setAttribute('id', todoItem.id);
    newTodoItem.classList.add('todo-box');
    todoContainer.appendChild(newTodoItem);
    var newTodoTextBox = document.querySelector('todo-box');
    var newTodoText = document.createElement('p');
    newTodoText.innerText = todoItem.text;
    newTodoItem.appendChild(newTodoText);

  });
}

function deleteForRefreshInHTML() {
  todoContainer.innerHTML= '';
}

var refresh = function() {
  deleteForRefreshInHTML();
  createRequest('GET', url, {}, listCallback);
}

var createTodoCallback = function(response) {
  refresh();
}

function deleteItemFromServer(id, callback) {
  var req = new XMLHttpRequest();
  req.open('DELETE', url + '/' + id);
  req.send();
  req.onreadystatechange = function() {
    if (req.readyState === 4) {
      var response = JSON.parse(req.response);
      return callback(response.id)
    }
  }
}

function deleteItemFromTodoList(id) {
  var deleteItem = document.getElementById(id);
  deleteItem.remove();
}


var listTodoItemsButton = document.querySelector('.list-todos-button');
var addnewTodoButton = document.querySelector('.add-new-todo-button');
var deleteTodoButton = document.querySelector('.delete-todo-button');
var textInput = document.querySelector('textarea');
var createButton = document.querySelector('.send-button');



listTodoItemsButton.addEventListener('click', function() {
  deleteTodoButton.classList.remove('active');
  textInput.classList.add('hidden');
  createButton.classList.add('hidden');
  refresh();
});

addnewTodoButton.addEventListener('click', function() {
  textInput.classList.remove('hidden');
  createButton.classList.remove('hidden');
  deleteTodoButton.classList.remove('active');
  refresh();
});

deleteTodoButton.addEventListener('click', function() {
  refresh();
  deleteTodoButton.classList.add('active');
  textInput.classList.add('hidden');
  createButton.classList.add('hidden');
});

createButton.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: textInput.value});
  createRequest('POST', url, newTodo, createTodoCallback);
  deleteTodoButton.classList.remove('active');
  textInput.classList.add('hidden');
  createButton.classList.add('hidden');
});

// var todoBoxes = querySelectorAll('.todo-box');
//
// todoBoxes.forEach(function(todoBox) {
//   todoBox.addEventListener('click', function(e) {
//     e.remove();
//   });
// });
