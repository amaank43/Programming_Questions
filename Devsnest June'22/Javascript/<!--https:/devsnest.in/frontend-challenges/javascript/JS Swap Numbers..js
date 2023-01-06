<!--https://devsnest.in/frontend-challenges/javascript/js-swap-numbers/185-->

let { num1, num2 } = require('./secret')
/* You are given two integers num1 and num2
Write logic inside function swap such that, whenever swap is called, it swaps num1 and num2's values
 */

function swap() {
	/* code from here */
let temp;
   temp =num2;
  num2=num1;
  num1=temp;

	/* to here */
}

swap()
try { module.exports = { swap, num1, num2 } } catch (e) { }
