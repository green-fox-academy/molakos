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
  'http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-59610.jpg',
  'img/code1.png',
  'img/code2.png',
  'img/code3.png'
]

var prev = document.querySelector('.prev');
var next = document.querySelector('.next');
var currentPicture = document.querySelector('.currentPicture');
var pictureIndex = 0;
var thumbnails = document.querySelector('.thumbnails');
currentPicture.setAttribute('src', images[pictureIndex]);


function pickPictureByClick(event) {
  inactivatePicture();
  pictureIndex = event.target.id;
  changePicture(images[pictureIndex]);
  document.getElementById(event.target.id).classList.add('actual');
}

function addPicturesToThumbnail() {
  for (var i = 0; i < images.length; i++ ) {
    var listedPicture = document.createElement('img');
    listedPicture.addEventListener('click', pickPictureByClick);
    listedPicture.setAttribute('src', images[i]);
    listedPicture.setAttribute('id', i);
    thumbnails.appendChild(listedPicture);
  }
}

function inactivatePicture() {
  document.querySelector('.actual').classList.remove('actual');
}

function activatePicture(pictureIndex) {
  document.getElementById(pictureIndex).classList.add('actual');
}

function changePicture(src) {
  currentPicture.setAttribute('src', src);
}

function pickNextPicture() {
  inactivatePicture();
  if (pictureIndex === images.length - 1) {
    pictureIndex = 0;
  } else {
    pictureIndex++;
  }
  changePicture(images[pictureIndex]);
  activatePicture(pictureIndex);
}

function pickPrevPicture() {
  inactivatePicture();
  if (pictureIndex === 0) {
    pictureIndex = images.length - 1;
  } else {
    pictureIndex--;
  }
  changePicture(images[pictureIndex]);
  activatePicture(pictureIndex);
}

prev.addEventListener('click', function() {
  pickPrevPicture();
});

next.addEventListener('click', function() {
  pickNextPicture();
});

addPicturesToThumbnail();
