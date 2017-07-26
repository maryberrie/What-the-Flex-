//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function hide(){
  $("#survey").css({"visibility":"hidden"})
}
function moveOn(){
  window.location.replace('/companion');
}
alert('test')

function setup(){
  $("#hide").click(hide);
  $("#replace").click(moveOn);
  $("survey").submit(moveOn);
}

$(document).ready(setup);
