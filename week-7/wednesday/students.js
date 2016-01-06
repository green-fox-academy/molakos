'use strict';

function Student(name, grades) {
  this.name = name;
  this.grades = [];
  this.addGrade = function(grade) {
    this.grades.push(grade);
  }
  this.getAverage = function(grades) {
    var grades = this.grades;
    var sum = grades.reduce(function(acc, num) {
      return acc + num;
    }, 0);
    return sum / grades.length;
  }
}

var jozsi = new Student('Jozsi');
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);

console.log(jozsi.grades);
console.log(jozsi.getAverage());
