<!--https://devsnest.in/frontend-challenges/javascript/js-default-parameter-value/187-->

/* Create a function getPerson, that have name, age, isEmployed
assign isEmployed a default value false
and return the details in form of a javascript object like given in the example in instructions */

/* Code from here */
function getPerson(name,age,isEmployed){
  return {
  name,
    age,
    isEmployed : false,
  
  }
}

/* to here */

try { module.exports = { getPerson } } catch (e) { } 
