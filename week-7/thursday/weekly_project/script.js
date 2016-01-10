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

function addPicturesToThumbnail(src) {
  var listedPicture = document.createElement('img');
  listedPicture.setAttribute('src', src);
  listedPicture.setAttribute('id', i)
  thumbnails.appendChild(listedPicture);
}

for (var i = 1; i < images.length; i++ ) {
  addPicturesToThumbnail(images[i]);
}

function changePicture(src) {
  currentPicture.setAttribute('src', src);
  // console.log(document.getElementsByClassName('id' + pictureIndex));

}



function pickNextPicture() {
  if (pictureIndex === images.length - 1) {
    pictureIndex = 0;
  } else {
    pictureIndex++;
  }
    changePicture(images[pictureIndex]);
}

function pickPrevPicture() {
  if (pictureIndex === 0) {
    pictureIndex = images.length - 1;
  } else {
    pictureIndex--;
  }
  changePicture(images[pictureIndex]);
}

prev.addEventListener('click', function() {
  pickPrevPicture();
});

next.addEventListener('click', function() {
  pickNextPicture();
});

thumbnails.addEventListener('click', function(event) {
  document.querySelector('.actual').classList.remove('actual');
  event.target.classList.add('actual')
  changePicture(event.target.getAttribute('src'));
})
