'use strict';

console.log('mukodik');
var cim = document.querySelector('h1');
console.log(cim);

// cim.style.backgroundColor = 'pink';

cim.classList.add('piros');

var majomKep = document.querySelector('img');

majomKep.setAttribute('src', 'https://media.giphy.com/media/EldfH1VJdbrwY/giphy.gif')

document.querySelector('body').appendChild(majomKep);

function kepcsinalo(src) {
  var valamiKep = document.createElement('img');

  valamiKep.setAttribute('src', src);

  var bodyvaltozoban = document.querySelector('body').appendChild(valamiKep);
}

// kepcsinalo('https://49.media.tumblr.com/4834c34c47276bdca42c136b8a6d0e9f/tumblr_ny343bknwt1sn75h6o1_400.gif');


// for (var i = 0; i < 11; i++) {
//   kepcsinalo('https://49.media.tumblr.com/4834c34c47276bdca42c136b8a6d0e9f/tumblr_ny343bknwt1sn75h6o1_400.gif');
// }

var kepek = ['https://media.giphy.com/media/vhsNmFjuN4WDS/giphy.gif', 'https://media.giphy.com/media/xT77Y4AVm5SWuhjJFC/giphy.gif', 'https://media.giphy.com/media/3o85xkqfu7tMeLyh8I/giphy.gif', 'http://lorempixel.com/400/200/transport', 'http://lorempixel.com/400/200/people', 'http://lorempixel.com/400/200/abstract', 'http://lorempixel.com/400/200/food', 'http://lorempixel.com/400/200/sports', 'http://lorempixel.com/400/200/city', 'http://lorempixel.com/400/200/cats']

// kepek.forEach(function(e) {
//   kepcsinalo(e)
// });


var gomba = document.querySelector('.csinal');

gomba.addEventListener('click', function() {
  kepcsinalo('http://lorempixel.com/400/200/cats');
});

window.addEventListener('scroll', function() {
  console.log('scroll', window.scrollY);
})

var cicat = document.querySelector('.cicat');
var kutyat = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.cicakutyakep');

cicat.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://lorempixel.com/400/200/cats')
});

kutyat.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://www.petfinder.com/wp-content/uploads/2012/11/122163343-conditioning-dog-loud-noises-632x475.jpg')
});
