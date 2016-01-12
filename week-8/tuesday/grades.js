'use strict';

var grades = [3, 4, 5, 2, 3, 5, 2, 5];


function countFives(gradesList) {
  var counts = 0;
  for (var i = 0; i < gradesList.length; i++) {
    if (gradesList[i] === 5) {
      counts++;
    }
  }
  return counts;
}

console.log(countFives(grades));
