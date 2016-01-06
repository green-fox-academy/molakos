'use strict';

function textMultiply(text, number) {
  var myWord = '';
  for (var i = 0; i < number; i++) {
    myWord += text
  }
  return myWord;
}

console.log(textMultiply('alma', 3));
