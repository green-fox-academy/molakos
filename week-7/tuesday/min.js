'use strict';

var numbers = [7, 8, -1, 4, 3, 12];
var minimum = numbers[0];

for (var i = 1; i <= numbers.length; i++) {
  if (minimum > numbers[i]) {
    minimum = numbers[i];
    console.log(minimum);
  }
}
