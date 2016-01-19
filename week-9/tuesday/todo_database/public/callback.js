'use strict';

function createRequest(method, url, data, callback) {
  var request = new XMLHttpRequest();
  request.open(method, url);
  request.setRequestHeader('Content-Type', 'application/json');
  request.send(data);
  request.onreadystatechange = function () {
    console.log('allapot: ', request.readyState);
    if (request.readyState === 4) {
      callback(request.response);
    }
  }
}
