function show(event){
  var input = $("#Enter").val().toLowerCase();
  if(input == "butterfly"){
    $("#survey").show();
    event.preventDefault();
  }else{
    window.location.href = "/companion";
    event.preventDefault();
  }
}

function moveToCompanion(){
  window.location.href="/companion";
}
function goBack(){
  window.history.back();
}

function goHome(){
  window.location.href = "/";
}
function setup(){
//  $("#test").click(show);
  $("#input").submit(show);
  //$("#replace").click(moveOn);
  $("survey").submit(moveToCompanion);
  $("#deer").click(goBack);
  $("#home").click(goHome);
}

$(document).ready(setup);
