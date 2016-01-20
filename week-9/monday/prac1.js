'use strict';

var array = ['apple', 'pear', 'melon', 'carrot'];

function deleteFromArray(array, item) {
  var newArray = []
  for (var i = 0; i < array.length; i++) {
    if (array[i] !== item) {
      newArray.push(array[i]);
    }
  }
  return newArray;
}


function delete2(array) {
  array.splice(array.indexOf('carrot'), 1);
  return array;
}

console.log(delete2(array));
