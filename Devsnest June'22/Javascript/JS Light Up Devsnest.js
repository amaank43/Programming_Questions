<!--https://devsnest.in/frontend-challenges/javascript/js-light-up-devsnest/163-->

/* Here you have to add a keydown event listener on window so that you can get 
information of which key is pressed and build logic around it.
Then you have to build logic such that, Each key press changes the color of its
corrosponsing letter ('letters are inside span tags, having class .letter').
Change it to the color provided below. 

Important ID(s): container's (div) id = 'container'
Important Class(s): class for span tags containing letters = 'letter' */
const COLOR = 'rgb(128, 128, 255)'

/* code from here */
function checkKey(key){
let vari  =document.getElementsByClassName('letter')
for(let item of vari){
if(item.innerText.toLowerCase()==key){
    item.style.color= COLOR;
    }
   }
  }
window.addEventListener('keydown', (e)=>{ checkKey (e.key)
})


/* to here */
