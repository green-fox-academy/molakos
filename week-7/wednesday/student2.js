'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = {};
  this.addGrade = function (subject, grade) {
    if (this.grades[subject] === undefined) {
      this.grades[subject] = [];
      this.grades[subject].push(grade);
    } else {
    } this.grades[subject].push(grade);
  }
  this.getCount = function () {
    var gradeCount = 0;
    Object.keys(this.grades).forEach(function(key, index) {
      gradeCount = index.length;
    });
    console.log(gradeCount);
  }
  this.getAverage = function() {
    var average = 0;
    this.grades.forEach(function(e) {
      average += e
    });
    return average / this.grades[subject].length;
  }
}

var dezso = new Student('Dezso');

dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
//console.log(dezso.grades);
// var sum = 0;
// for(var subject in dezso.grades) {
//   console.log(subject);
//   dezso.grades.subject.forEach(function (e) {
//     sum += 1
//   });
// }
// console.log(sum);
//console.log(dezso.grades);

dezso.getCount() // 'rajz: 2', matek: 3
//dezso.getAverage() // 3.4

//szorgalmi
// dezso.getAverageBySubject() 'matek': 4.3, 'rajz': 2
