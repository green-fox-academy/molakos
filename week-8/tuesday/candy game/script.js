'use strict';

var candyCount = 0;
var lollyCount = 0;
var candyPerSecond = 0;
var priceForChange = 10;
var createCandyButton = document.querySelector('.create-candy');
var buyLollipopButton = document.querySelector('.buy-lollipop');
var numberOfCandies = document.querySelector('.candies');
var numberOfLollipops = document.querySelector('.lollipops');
var numberOfCandiesPerSecond = document.querySelector('.candies-per-second');

function createCandies() {
  candyCount++;
}

function buyLollipops() {
  if (candyCount >= priceForChange) {
    lollyCount++;
    candyCount -= priceForChange;
  }
}

function countCandiesPerSecond() {
  candyPerSecond = Math.floor(lollyCount / priceForChange);
  return candyPerSecond;
}

function updateCandies() {
  numberOfCandies.innerHTML = candyCount;
}

function updateLollipops() {
  numberOfLollipops.innerHTML = lollyCount;
}

function updateCandyPerSecond() {
  numberOfCandiesPerSecond.innerHTML = countCandiesPerSecond();
}

function checkIfStillDisabled() {
  if (candyCount >= priceForChange) {
    buyLollipopButton.removeAttribute('disabled');
  }
  if (candyCount < priceForChange) {
    buyLollipopButton.setAttribute('disabled', 'disabled');
  }
}

setInterval(function() {
  candyCount += countCandiesPerSecond();
  updateCandies();
  updateCandyPerSecond();
  if (candyCount === 10000) {
    alert('You win!');
  }
}, 1000);

setInterval(function() {
  checkIfStillDisabled();
}, 50);


createCandyButton.addEventListener('click', function() {
  createCandies();
  updateCandies();
  checkIfStillDisabled();
});

buyLollipopButton.addEventListener('click', function() {
  buyLollipops();
  updateCandies();
  updateLollipops();
});
