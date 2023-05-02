<!--https://devsnest.in/frontend-challenges/javascript/js-includes-even/209

// you're given an arr as parameter to the function `includesEven`
// use Array.some() to check if there exists any even number in
// the array `arr`
// and return the result from the function `includesEven`


function includesEven(arr) {
	// code here
	const even = (element) => element % 2 === 0 
    return arr.some(even)
}


try { module.exports = { includesEven } } catch(e) {}
