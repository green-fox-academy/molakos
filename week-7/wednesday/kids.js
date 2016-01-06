'use strict';

var kids = [
  {name: 'Tibbor', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Juli', candies: 7},
  {name: 'Krisztian', candies: 4},
];

function getTheRichestKidsName(kids) {
  var richestKid = kids[0];
  for (var i = 0; i < kids.length; i++) {
    if (richestKid.candies < kids[i].candies){
      richestKid = kids[i];
    }
  }
  return richestKid.name;
}

console.log(getTheRichestKidsName(kids));


function getTheRichestKidsName2(kids) {
  var richestKid = kids[];
  kids.forEach(function(currentKid){
    if (richestKid.candies < currentKid.candies){
      richestKid = currentKid;
  });
  return richestKid.name;
}

console.log(getTheRichestKidsName2(kids))
