
window.onload=function(){

var sidebar = document.getElementById("mySidebar")
var btn = document.getElementById("doom")
var main = document.getElementById("main")

btn.addEventListener("click",fur);


function fur() {
  
  if(sidebar.style.width == "0px"){

    sidebar.style.width = "250px";
    main.style.marginLeft = "250px";

  }
   
  else {
  
  sidebar.style.width = "0px";
  main.style.marginLeft = "0px";
  
}
}










}



