//function show(){
//  $("#survey").css({"visibility": "visible"});
//}
function show(event){
  var input = $("#Enter").val();
  if(input == "butterfly"){
    $("#survey").show();
    event.preventDefault();
  }else{
    window.location.href = "/companionsunshine";
    event.preventDefault();
  }
}

function moveToCompanion(){
  window.location.href = "/companionsunshine";
}
function goBack() {
    window.history.back();
}

function setup(){
//  $("#test").click(show);
  $("#input").submit(show);
  //$("#replace").click(moveOn);
  $("survey").submit(moveToCompanion);
  $("#rabbit").click(goBack);
}

$(document).ready(setup);
