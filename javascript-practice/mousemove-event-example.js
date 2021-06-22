document.write("hello");
document.addEventListener("mousemove", function(event) {
  myFunction(event);
});

function myFunction(e) {
  var x = e.clientX;
  var y = e.clientY;
  var coor = "Coordinates: (" + x + "," + y + ")";
  document.body.innerHTML = coor;
}
