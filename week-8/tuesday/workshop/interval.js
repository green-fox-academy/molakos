'use strict';

var count = 0;

var interval = setInterval(function() {
  count++;
  console.log('jejjejeeje', count);
}, 500);


setTimeout(function() {
  console.log('Boom');
  clearInterval(interval);
}, 5000);


setTimeout(function() {
  for (var i = 0; i < 1231231241; i++)
}, 2000);
