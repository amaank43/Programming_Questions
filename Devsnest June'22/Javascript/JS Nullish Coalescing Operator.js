<!--https://devsnest.in/frontend-challenges/javascript/js-nullish-coalescing-operator/201-->

// you are given a variable value as parameter of 
// function devsnest, value can also be null
// in case value is null return string 'value is null' 
// from the function devsnest
// Note: 
// you have to useNullish coalescing operator (??) for this task


function devsnest(value) {
   // code here
  const valA = value ?? "value is null"; return valA;
}


try { module.exports = { devsnest } } catch(e) {}
