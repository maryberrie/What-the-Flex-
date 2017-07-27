//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function show(event){
  var input = $("#Enter").val();
  if(input == "butterfly"){
    $("#survey").show();
    event.preventDefault();
  }else{
    window.location.replace('/companionsunshine');
    event.preventDefault();
  }
}

function moveToCompanion(){
  window.location.replace('/companionsunshine');
}

function setup(){
//  $("#test").click(show);
  $("#input").submit(show);
  //$("#replace").click(moveOn);
  $("survey").submit(moveToCompanion);
}

$(document).ready(setup);
