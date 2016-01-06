'use strict';

function reverser(name) {
  var reversed = '';
  for (var i = name.length-1; i >= 0; i--) {
    reversed += name[i];
  }
  return reversed;s
}

console.log(reverser('kacsa'));

// recursive

function reverse2(input) {
  return reverseRecursive(input, input.length-1);
}

function reverseRecursive(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input[i] + reverseRecursive(input, i - 1);
  }
}


console.log(reverseRecursive('kacsa', 4))
