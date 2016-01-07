'use strict';

var images = [
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-198979.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-306637.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-137114.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-110644.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-162286.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-178808.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-72799.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-68356.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-187019.jpg',
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-59610.jpg'
]

var prev = document.querySelector('.prev');
var next = document.querySelector('.next');
var currentPicture = document.querySelector('.currentPicture');

function changePicture(src) {
  currentPicture.setAttribute('src', src);
}

var pictureIndex = 0;

function pickNextPicture() {
  if (pictureIndex === images.length - 1) {
    pictureIndex = 0;
    changePicture(images[pictureIndex])
    console.log(images[pictureIndex]);
  } else {
    console.log(images[pictureIndex]);
    pictureIndex++;
    changePicture(images[pictureIndex]);
  }
}

function pickPrevPicture() {
  if (pictureIndex === 0) {
    pictureIndex = images.length - 1;
    changePicture(images[pictureIndex])
  } else {
    pictureIndex--;
    changePicture(images[pictureIndex]);
  }
}

prev.addEventListener('click', function() {
  pickPrevPicture();
});

next.addEventListener('click', function() {
  pickNextPicture();
});
