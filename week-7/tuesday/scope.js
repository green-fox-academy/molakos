'use strict';

var g = 123;

function printG() {
  console.log(g);
  g = 333;
}

printG();
console.log(g);


function printLocalG() {
  var g = 7;
  console.log(g);
}

printLocalG();
console.log(g);









function printA() {
  var a = 111;
  console.log(a)
}

printA();
//  console.log(a); ---> this will throw an error, cuz its not defined == function scope ==
