//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function show(event){

  console.log("test");
  var input = $("#Enter").val();
  console.log(input);
  if(input == "butterfly"){
    $("#survey").show();
    console.log("second");

  }
  event.preventDefault();
}

function moveToCompanion(){
  window.location.replace('/companion');
}

function setup(){
//  $("#test").click(show);
  $("#input").submit(show);
  //$("#replace").click(moveOn);
  $("survey").submit(moveToCompanion);
}

$(document).ready(setup);
