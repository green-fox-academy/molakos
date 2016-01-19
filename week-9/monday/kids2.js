'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function countBySex(kids) {
  var sex = {female: 0, male: 0}
  kids.forEach(function(kid) {
    if (kid.sex === 'female') {
      sex.female++;
    } else if (kid.sex === 'male') {
      sex.male++;
    }
  });
  return sex;
}

// console.log(countBySex(kids));

function countBySex2(kids) {
  var sex = {female: 0, male: 0}
  kids.forEach(function(kid) {
    sex[kid.sex]++
  });
  return sex;
}

// console.log(countBySex2(kids));

function countBySex3(kids) {
  var sex = {}
  kids.forEach(function(kid) {
    if (sex[kid.sex] === undefined) {
      sex[kid.sex] = 0;
    }
    sex[kid.sex]++
  });
  return sex;
}

console.log(countBySex3(kids));
