'use strict';

var humwee = {
  km: 20000,
  type: 'Rendes katonai hummer',
  color: 'terep',
  ride: ride
};

console.log(humwee.km)

function ride(km) {
  this.km += km;
}

humwee.ride(200);

console.log(humwee.km);


var humwee2 = {
  km: 20000,
  type: 'Rendes katonai hummer',
  color: 'terep',
  ride: function(km) {
    this.km += km;
  }
};

console.log(humwee.km)



humwee2.ride(200);

console.log(humwee2.km);
console.log(humwee2);
