'use strict';

var fs = require('fs');

function countLetterInAlmaTxt(letter, callback) {
  fs.readFile('alma.txt', function(err, content) {
    var count = 0;
    var stringContent = String(content);
    for (var i = 0; i < stringContent.length; i++) {
      if (letter === stringContent[i]) {
        count++;
      }
    }
    callback(count);
  });
}


countLetterInAlmaTxt('a', function(count) {
  console.log(count);
});
