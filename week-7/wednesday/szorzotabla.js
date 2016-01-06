'use strict';

function multiboard(number) {
  var output = '';
  for (var i = 1; i <= 10; i++) {
    output += (number + ' * ' + i + ' = ' + number * i + '\n');
  }
  return output
}

for (var i = 1; i <= 10; i++) {
  console.log(multiboard(i));
}


function recSzorzo(number, i) {
  if (i > 10) {
    return '';
  }
  return i + '*' + number + '=' + number * i +'\n' + recSzorzo(number, i + 1)
}

console.log(recSzorzo(4, 1));

// console.log(' ');

// function mySqrt() {
//   for (var i = 1; i <= 10; i++) {
//     console.log(String(i) + ' * ' + String(i) + ' = ' + i * i)
//   }
// }


// mySqrt()
