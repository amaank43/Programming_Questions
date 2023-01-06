<!--https://devsnest.in/frontend-challenges/javascript/js-fruit-apply/182-->

const { fruitBasket, threeFruits } = require('./secret')
/* use Function.prototype.apply() on the function `getFruitBasketInfo`
such that the function returns a string that returns basketId, fruitOne, fruitTwo, fruitThree  
and store it into the variable `result`
Note: 
fruitBasket contains basketId
threeFruits is a list of three fruit names as strings */

function getFruitBasketInfo(fruitOne, fruitTwo, fruitThree) {
  return this.basketId + ': ' + fruitOne + ' ' + fruitTwo + ' ' + fruitThree
}


//store the result in this variable
var result = getFruitBasketInfo.apply(fruitBasket,threeFruits, ['fruitOne' + 'fruitTwo' + 'fruitThree'])



/* code from here */


/* to here */

try { module.exports = { result, getFruitBasketInfo } } catch (e) { }
