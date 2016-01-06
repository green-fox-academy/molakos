'use strict'

var i = 0;

while (i <= 10) {
  console.log(i++);
  if (i === 4) {
    break;
  }
}

var myArray = ['kecske', 'dinnye', 'kfc'];

var j = 0;
while (j < myArray.length) {
  console.log(myArray[j]);
  j++;
}
