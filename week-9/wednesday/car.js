'use strict';

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;

  this.ride = function(km) {
    this.km += km;
  }
}



function Car2(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
}

Car2.prototype.ride = function(km) {
  this.km += km;
}

var trabi = new Car2('zold', 'Trabant', 400);

trabi.ride(0.02);

console.log(trabi.km);
