'use strict';


function runIn5Seconds(callback) {
  setTimeout(function(callback), 5000);
}

runIn5Seconds(function() {
  console.log('jeej');
});
