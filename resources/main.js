//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function hide(){
  $("#survey").css({"visibility":"hidden"})
}




function setup(){
  $("#show").click(show);
  $("#hide").click(hide);
}

$(document).ready(setup);
