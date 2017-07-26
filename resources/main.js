//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function hide(){
  $("#survey").css({"visibility":"hidden"})
}



function setup(){
  $("#hide").click(hide);
}

$(document).ready(setup);
