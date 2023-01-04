<!--https://devsnest.in/frontend-challenges/javascript/js-traffic-light/153-->

const lightone=document.getElementById("light-one");
const lightonecolor=window.getComputedStyle(lightone).getPropertyValue('background-Color');

const lighttwo=document.getElementById("light-two");
const lighttwocolor=window.getComputedStyle(lighttwo).getPropertyValue('background-Color');

const lightthree=document.getElementById("light-three");
const lightthreecolor=window.getComputedStyle(lightthree).getPropertyValue('background-Color');



lightone.style.backgroundColor=lightthreecolor;
lighttwo.style.backgroundColor=lightonecolor;
lightthree.style.backgroundColor=lighttwocolor;
