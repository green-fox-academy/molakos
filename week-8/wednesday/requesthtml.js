'use strict';

var ACCES_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';

var url = 'https://yoda.p.mashape.com/yoda';
var yodaButton = document.querySelector('.yoda-button');
var yodaInput = document.querySelector('.yoda-input');
var responseContainer = document.querySelector('.yoda-response');

function onDone(response) {
  responseContainer.innerText = response;
}

function createRequest (url, callback) {
  var probeRequest = new XMLHttpRequest();
  probeRequest.open('GET', url);
  probeRequest.setRequestHeader('X-Mashape-Key', ACCES_TOKEN);
  probeRequest.send();
  probeRequest.onreadystatechange = function () {
    console.log('allapot: ', probeRequest.readyState);
    if (probeRequest.readyState === 4) {
      callback(probeRequest.response)
    }
  }
}

yodaButton.addEventListener('click', function() {
  var sentence = yodaInput.value;
  var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);
  responseContainer.innerText = 'loading...';
  createRequest(urlWithParams, onDone)
})
