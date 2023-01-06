<!--https://devsnest.in/frontend-challenges/javascript/js-fruit-bind/181-->

const { fruit } = require('./secret')
/* use Function.prototype.bind() on the function `getFruitName` 
Such that it gives the function that returns fruitName of the provided fruit object 
Store the new function in the given variable `resultingFunction` */

function getFruitName() {
  return this.fruitName
}

// store the result in this variable
var resultingFunction = getFruitName.bind(fruit);

/* code from here */

/* to here */
try { module.exports = { resultingFunction, getFruitName } } catch (e) { }
