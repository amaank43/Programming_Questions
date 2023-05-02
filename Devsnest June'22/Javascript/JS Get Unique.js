<!--https://devsnest.in/frontend-challenges/javascript/js-get-unique/206-->

// arr of function getUnique's parameter is an array of duplicate characters
// create a Set out of arr to get unique values
// then convert it into an array and return that array of unique
// value to complete this task


function getUnique(arr) {
	// code here
	const mySet = new Set(arr);
 return (Array.from(mySet));
}


try { module.exports = { getUnique } } catch(e) {}
