'use strict';

var url = 'http://localhost:3000/todos';
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
    newTodoItem.appendChild(newTodoText)
    newTodoItem.addEventListener('dblclick', deleteItemFromTodoList);
  });
}

function refreshInHtml() {
  todoContainer.innerHTML= '';
}

var refresh = function() {
  refreshInHtml();
  createRequest('GET', url, {}, listCallback);
}

var createTodoCallback = function(response) {
  refresh();
}

function createDeleteRequest(id) {
  var req = new XMLHttpRequest();
  req.open('DELETE', url + '/' + id);
  req.send();
}

function deleteItemFromTodoList(id) {
  createDeleteRequest(event.target.id);
  refresh();
}


var listTodoItemsButton = document.querySelector('.list-todos-button');
var addnewTodoButton = document.querySelector('.add-new-todo-button');
var deleteTodoButton = document.querySelector('.delete-todo-button');
var textInput = document.querySelector('textarea');
var createButton = document.querySelector('.send-button');


function addClassToDOM(DOMName, className) {
  DOMName.classList.add(className);
}

function removeClassFromDOM(DOMName, className) {
  DOMName.classList.remove(className);
}

listTodoItemsButton.addEventListener('click', function() {
  removeClassFromDOM(deleteTodoButton, 'active');
  addClassToDOM(textInput, 'hidden');
  addClassToDOM(createButton, 'hidden');
  refresh();
});

addnewTodoButton.addEventListener('click', function() {
  removeClassFromDOM(textInput, 'hidden');
  removeClassFromDOM(createButton, 'hidden');
  removeClassFromDOM(deleteTodoButton, 'active');
  refresh();
});

// deleteTodoButton.addEventListener('click', function() {
//   var selectedItems = document.querySelectorAll('selected');
//   selectedItems.forEach(function(item) {
//     deleteItemFromTodoList();
//   });
// });

createButton.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: textInput.value});
  createRequest('POST', url, newTodo, createTodoCallback);
  removeClassFromDOM(deleteTodoButton, 'active');
  addClassToDOM(textInput, 'hidden');
  addClassToDOM(createButton, 'hidden');
});

// var todoBoxes = querySelectorAll('.todo-box');
//
// todoBoxes.forEach(function(todoBox) {
//   todoBox.addEventListener('click', function(e) {
//     e.remove();
//   });
// });
