'use strict';

function add(a, b) {
  return a + b;
}

console.log(add(1, 2))

var osszead = add;
console.log(osszead(4, 5));


var szorzas = function (a, b) {
  return a * b;
};

console.log(szorzas(4, 5));


var car = {
  km : 100,
  type : 'Skoda',
  honk : function () {
    console.log('Duuu');
  }
}


car.honk();
