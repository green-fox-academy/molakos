'use strict';

var createCandyButton = document.querySelector('.create-candy');
var buyLollipopButton = document.querySelector('.buy-lollipop');
var numberOfCandies = document.querySelector('.candies');
var numberOfLollipops = document.querySelector('.lollipops');
var numberOfCandiesPerSecond = document.querySelector('.candies-per-second');
var magicButton = document.querySelector('.for-hundred')

function CandyGame() {
  var that = this;
  this.candyCount = 98;
  this.lollyCount = 0;
  this.candyPerSecond = 0;
  this.priceForChange = 10;

  this.createCandies = function() {
    this.candyCount++;
  }
  this.buyLollipops = function() {
    if (this.candyCount >= this.priceForChange) {
      this.lollyCount++;
      this.candyCount -= this.priceForChange;
    }
  }
  this.countCandiesPerSecond = function() {
    this.candyPerSecond = Math.floor(this.lollyCount / this.priceForChange);
    return this.candyPerSecond;
  }
  this.updateCandies = function() {
    numberOfCandies.innerHTML = this.candyCount;
  }
  this.updateLollipops = function() {
    numberOfLollipops.innerHTML = this.lollyCount;
  }
  this.updateCandyPerSecond = function() {
    numberOfCandiesPerSecond.innerHTML = this.countCandiesPerSecond();
  }
  this.checkIfChangeAvailable = function() {
    if (this.candyCount >= this.priceForChange) {
      buyLollipopButton.removeAttribute('disabled');
    }
    if (this.candyCount < this.priceForChange) {
      buyLollipopButton.setAttribute('disabled', 'disabled');
    }
  }

  this.activateMagicButton = function() {
    if (this.candyCount >= 100) {
      magicButton.classList.remove('hidden');
    }
    if (this.candyCount < 100) {
      magicButton.classList.add('hidden');
    }
  }

  this.startGame = function() {
    setInterval(function() {
      that.candyCount += that.countCandiesPerSecond();
      that.updateCandies();
      that.updateCandyPerSecond();
      if (that.candyCount >= 10000) {
        alert('You win!');
        that.candyCount = 0;
        that.lollyCount = 0;
        that.candyPerSecond = 0;
      }
    }, 1000);

    setInterval(function() {
      that.checkIfChangeAvailable();
      that.activateMagicButton();
    }, 50);

    createCandyButton.addEventListener('click', function() {
      that.createCandies();
      that.updateCandies();
      that.checkIfChangeAvailable();
    });

    buyLollipopButton.addEventListener('click', function() {
      that.buyLollipops();
      that.updateCandies();
      that.updateLollipops();
    });

    magicButton.addEventListener('click', function() {
      if (that.candyCount >= 100) {
        that.lollyCount += 10;
        that.candyCount -= 100;
      }
      that.updateCandies();
      that.updateLollipops();
    })
  }
}

var playGame = new CandyGame;
playGame.startGame();
