<!--https://devsnest.in/frontend-challenges/javascript/js-add-boxes/151-->

for(let i=0;i<4;i++){
  const node = document.createElement("div");
  node.style.width = "75px";
   node.style.height = "75px";
  node.style.backgroundColor = "palevioletred";
  document.getElementById("container").appendChild(node);
}
