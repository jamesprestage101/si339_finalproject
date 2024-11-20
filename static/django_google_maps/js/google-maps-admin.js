function googleMapAdmin() {
    var autocomplete;
    var geocoder = new google.maps.Geocoder();
    var map;
    var marker;

    var geolocationId = 'id_geolocation';
    var addressId = 'id_address';

    var self = {
        initialize: function() {
            var lat = 0;
            var lng = 0;
            var zoom = 2;

            var existinglocation = self.getExistingLocation();
            if (existinglocation) {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 18;
            }

            var latlng = new google.maps.LatLng(lat, lng);
            var myOptions = {
                zoom: zoom,
                center: latlng,
                mapTypeId: self.getMapType()
            };
            map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

            if (existinglocation) {
                self.setMarker(latlng);
            }

            autocomplete = new google.maps.places.Autocomplete(
                document.getElementById(addressId),
                self.getAutoCompleteOptions()
            );

            autocomplete.addListener("place_changed", self.codeAddress);

            $("#" + addressId).keydown(function(e) {
                if (e.keyCode === 13) {
                    e.preventDefault();
                    return false;
                }
            });
        },

        getAutoCompleteOptions: function() {
            var geolocation = document.getElementById(addressId);
            var autocompleteOptions = geolocation.getAttribute('data-autocomplete-options');

            if (!autocompleteOptions) {
                return { types: ['geocode'] };
            }

            return JSON.parse(autocompleteOptions);
        },

        setMarker: function(latlng) {
            if (marker) {
                marker.setPosition(latlng);
            } else {
                marker = new google.maps.Marker({
                    map: map,
                    position: latlng,
                    draggable: true
                });
                self.addMarkerDrag(marker);
            }
        },

        addMarkerDrag: function(marker) {
            google.maps.event.addListener(marker, 'dragend', function(new_location) {
                self.updateGeolocation(new_location.latLng);
            });
        },

        getExistingLocation: function() {
            var geolocation = document.getElementById(geolocationId);
            if (!geolocation || !geolocation.value) {
                return [53.3522908033196, -6.257729843109473]; // Default to Ireland
            }
            return geolocation.value.split(',').map(parseFloat);
        },

        codeAddress: function() {
            var place = autocomplete.getPlace();
            if (place.geometry) {
                self.updateWithCoordinates(place.geometry.location);
            } else {
                geocoder.geocode({ address: place.name }, function(results, status) {
                    if (status === google.maps.GeocoderStatus.OK) {
                        self.updateWithCoordinates(results[0].geometry.location);
                    } else {
                        alert("Geocode failed: " + status);
                    }
                });
            }
        },

        updateWithCoordinates: function(latlng) {
            map.setCenter(latlng);
            map.setZoom(18);
            self.setMarker(latlng);
            self.updateGeolocation(latlng);
        },

        updateGeolocation: function(latlng) {
            document.getElementById(geolocationId).value = `${latlng.lat()},${latlng.lng()}`;
            $("#" + geolocationId).trigger('change');
        },

        getMapType: function() {
            return google.maps.MapTypeId.ROADMAP;
        }
    };

    return self;
}

$(document).ready(function() {
    var googlemap = googleMapAdmin();
    googlemap.initialize();
});
