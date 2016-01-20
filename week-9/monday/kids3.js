'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];


function groupBySex(kids) {
  var groups = {female :[], male:[]};
  kids.forEach(function(kid) {
    if (kid.sex === 'female') {
      groups.female.push(kid);
    } else {
      groups.male.push(kid);
    }
  });
  return groups;
}

// console.log(groupBySex(kids));

function groupBySex3(kids) {
  var groups = {female :[], male:[]};
  kids.forEach(function(kid) {
    groups[kid.sex].push(kid);
  });
  return groups;
}

// console.log(groupBySex3(kids));

function groupBySex2(kids) {
  var groups = {}
  kids.forEach(function(kid) {
    if (groups[kid.sex] === undefined) {
      groups[kid.sex] = [];
    }
    groups[kid.sex].push(kid);
  });
  return groups;
}

console.log(groupBySex2(kids));
