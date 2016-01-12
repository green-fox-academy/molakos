'use strict';

var tape = require('tape');

var arabic2troman = require('./kata');

tape('roman converter', function(t) {
  //t.equal(actual, expected);
  t.equal(arabic2troman(0), '');
  t.equal(arabic2troman(1), 'I');
  t.equal(arabic2troman(2), 'II');
  t.equal(arabic2troman(4), 'IV');
  t.equal(arabic2troman(5), 'V');
  t.equal(arabic2troman(6), 'VI');
  t.equal(arabic2troman(7), 'VII');
  t.equal(arabic2troman(8), 'VIII');
  t.equal(arabic2troman(9), 'IX');
  t.equal(arabic2troman(10), 'X');
  t.equal(arabic2troman(11), 'XI');
  t.equal(arabic2troman(12), 'XII');
  t.equal(arabic2troman(23), 'XXIII');
  t.equal(arabic2troman(43), 'XLIII');
  t.equal(arabic2troman(103), 'CIII');
  t.equal(arabic2troman(467), 'CDLXVII');
  t.equal(arabic2troman(917), 'CMXVII');





  t.end();
});
