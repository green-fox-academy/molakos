'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function getAgeByName(kidsList, name) {
  for (var i = 0; i < kidsList.length; i++) {
    if (kidsList[i].name === name) {
      return kidsList[i].age;
    }
  }
}

function getAgeByName2(kidsList, name) {
  var storedKid = {}
  kidsList.forEach(function(kid) {
    if (kid.name === name) {
      storedKid = kid;
    }
  });
  return storedKid.age;
}

// console.log(getAgeByName(kids, 'Gerda'));


function countByAge(kids, age) {
  var kidsWithSelectedAge = 0;
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].age === age) {
      kidsWithSelectedAge++;
    }
  }
  return kidsWithSelectedAge;
}

// console.log(countByAge(kids, 8));

function getAges(kids) {
  var ages = [];
  kids.forEach(function(kid) {
    ages.push(kid.age);
  });
  return ages;
}

function getAges2(kids) {
  return kids.map(function(kid) {
    return kid.age;
  });
}

// console.log(getAges2(kids));

function getTheLongestNamesAge(kids) {
  var longestName = kids[0];
  kids.forEach(function(kid) {
    if (kid.name.length > longestName.name.length) {
      longestName = kid;
    }
  });
  return longestName.age;
}

console.log(getTheLongestNamesAge(kids));
