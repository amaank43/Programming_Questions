<!--https://devsnest.in/frontend-challenges/javascript/js-frequency-map/207-->

// `arr` parameter of function `getFrequencyMap` 
// is an array of duplicate integers
// Create a Map that contains count of every number that exists in 
// the array `arr` and return it via function `getFrequencyMap`


function getFrequencyMap(arr) {
	// code here
 var mp = new Map();
 for (var i = 0; i<arr.length; i++){
    if(mp.has(arr[i]))
      mp.set(arr[i], mp.get(arr[i])+1)
    else
      mp.set(arr[i], 1)
  }
  return mp

}


try { module.exports = { getFrequencyMap } } catch(e) {}
