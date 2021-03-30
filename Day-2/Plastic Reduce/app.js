var lat = 0
var long = 0

var x = document.getElementById("location");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
        console.log("pop")
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {

    if (lat == 0 && long == 0) {
        lat = position.coords.latitude;
        long = position.coords.longitude;
    }

    console.log("hello")
    x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;

    if (findiflong(position.coords.latitude, position.coords.longitude) > 2)
        alert("Hey you seems to go out! Beaware to not take plastic bag from outside!!!");
}


function findiflong(a, b) {
    lat1 = a
    lon1 = b
    lat2 = lat
    lon2 = long
    var p = 0.017453292519943295;    // Math.PI / 180
    var c = Math.cos;
    var a = 0.5 - c((lat2 - lat1) * p) / 2 +
        c(lat1 * p) * c(lat2 * p) *
        (1 - c((lon2 - lon1) * p)) / 2;

    return 12742 * Math.asin(Math.sqrt(a));
}