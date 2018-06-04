// initialize Google map
function myMap() {
  // Liverpool Guild of Students coordinates: 53.405222,-2.966088
  var myCenter = new google.maps.LatLng(53.405222,-2.966088);
  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 13};
  var map = new google.maps.Map(mapCanvas, mapOptions);
  var marker = new google.maps.Marker({position:myCenter});
  marker.setMap(map);
}

// add functionality to email form here
