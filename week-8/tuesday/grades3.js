var grades = [
  {num: 3, subject: 'math'},
  {num: 5, subject: 'math'},
  {num: 5, subject: 'arts'},
  {num: 2, subject: 'sport'},
  {num: 5, subject: 'physics'},
  {num: 4, subject: 'physics'},
  {num: 5, subject: 'math'},
];

function countMathFives(gradesList) {
  var output = 0;
  gradesList.forEach(function(grade) {
    if (grade.num === 5 && grade.subject === 'math') {
      output++;
    }
  });
  return output;
}

console.log(countMathFives(grades));
