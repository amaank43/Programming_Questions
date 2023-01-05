<!--https://devsnest.in/frontend-challenges/javascript/js-create-counter/178-->





/* Create a class named Counter with non-static property count and a member function increment
& -- Read the given instructions -- */

/* Code from here */
class Counter
{
constructor()
{
this.count = 0 ;
} 
  increment() 
{
this.count=+1 ;
}
}

/* to here */

try { module.exports = { Counter } } catch (e) { }
