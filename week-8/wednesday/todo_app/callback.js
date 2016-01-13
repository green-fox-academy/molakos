'use strict';

function createRequest(method, url, data, callback) {
  var probeRequest = new XMLHttpRequest();
  probeRequest.open(method, url);
  probeRequest.setRequestHeader('Content-Type', 'application/json');
  probeRequest.send(data);
  probeRequest.onreadystatechange = function () {
    console.log('allapot: ', probeRequest.readyState);
    if (probeRequest.readyState === 4) {
      callback(probeRequest.response);
    }
  }
}
