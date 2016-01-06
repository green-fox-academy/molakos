'use strict';

var numList = [1, 2, 3, 4, 5, 6]


function calculateSum(list) {
  var summ = 0
  for (var i = 0; i < list.length; i++) {
    summ += list[i];
  }
  return summ;
}

console.log(calculateSum(numList));
