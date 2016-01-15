'use strict';

var pirates = [
  {name: 'Jack', id: 1},
  {name: 'Bob', id: 2},
  {name: 'Omar', id: 3},
  {name: 'Olaf', id: 4},
  {name: 'Boris', id: 5}
];

var stashes = [
  {pirateId: 3, gold:4},
  {pirateId: 4, gold:1},
  {pirateId: 2, gold:5},
  {pirateId: 5, gold:3},
  {pirateId: 1, gold:8},
];

function getGoldByPirateName(pirateName) {
  var storedByName = {};
  pirates.forEach(function(pirate) {
    if (pirate['name'] === pirateName) {
      storedByName = pirate;
    }
  });
  var output = 0;
  stashes.forEach(function(stash) {
    if (stash['pirateId'] === storedByName['id']) {
      output = stash['gold'];
    }
  });
  return output;
}

function getGoldByPirateName2(pirateName) {
  var storedByName = getIdByName(pirateName);
  var output = 0;
  stashes.forEach(function(stash) {
    if (stash['pirateId'] === storedByName['id']) {
      output = stash['gold'];
    }
  });
  return output;
}

function getIdByName(pirateName) {
  var storedByName = {};
  pirates.forEach(function(pirate) {
    if (pirate['name'] === pirateName) {
      storedByName = pirate;
    }
  });
  return storedByName;
}

console.log(getGoldByPirateName('Olaf'));
console.log(getGoldByPirateName2('Olaf'));
