//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function show(event){
  var input = $("#Enter").val().toLowerCase();
  if(input == "butterfly"){
    $("#survey").show();
    event.preventDefault();
  }else{
    window.location.href= "/companion";
  }
}

function moveToCompanion(){
  window.location.href="/companion";
}

function setup(){
//  $("#test").click(show);
  $("#input").submit(show);
  //$("#replace").click(moveOn);
  $("survey").submit(moveToCompanion);
}

$(document).ready(setup);
