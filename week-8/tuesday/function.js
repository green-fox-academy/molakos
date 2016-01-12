'use strict';
//
// var button = document.querySelector('button');
//
// button.addEventListener('click', shout);
//
// function shout() {
//   alert('ajjajajaajjaj');
//   alert('ajjajajaajjaj');
//   alert('ajjajajaajjaj');
//   alert('ajjajajaajjaj');
//   alert('ajjajajaajjaj');
//   alert('ajjajajaajjaj');
// }
//


var human = {
  word: ['kacsa', 'macska', 'mammlasz'],
  name: 'Tibbor'
  speak: speak
}

function speak() {
  var _this = this
  this.word.forEach(function(w) {
    console.log('I am ' + _this.name);
    console.log('blablabla' + w);
  });
}

speak();
