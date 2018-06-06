// initialize Google map
function myMap() {
  // Liverpool Guild of Students coordinates: 53.405222,-2.966088
  var myCenter = new google.maps.LatLng(53.405222,-2.966088);
  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 13};
  const map = new google.maps.Map(mapCanvas, mapOptions);
  const marker = new google.maps.Marker({position:myCenter});
  marker.setMap(map);
}

// Ensures user input data into all input fields
const validateInput = () => {
  var form = document.getElementById("contact-form");
  var inputs = form.querySelectorAll("input, textarea");

  for (i = 0; i < inputs.length; i++) {
      var inputValue = inputs[i].value;
      if (inputValue == "" || inputValue == null) {
          alert("Please ensure that all field contains relevant input data");
          return false;
      }
  }
  return true;
}
