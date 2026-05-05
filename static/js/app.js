var tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    minZoom: 2,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
var latlng = L.latLng(23.817064, 120.958004);
var map = L.map('map', {
    center: latlng,
    zoom: 8,
    zoomControl: false,
    layers: [tiles]
});

new L.Control.FullScreen({
    position: 'topleft',
    title: '全螢幕',
    titleCancel: '離開全螢幕',
    forceSeparateButton: true
}).addTo(map);
var markers = L.markerClusterGroup();
var markerList = [];
var controlSearch = new L.Control.Search({
    position: 'topright',
    layer: markers,
    initial: true,
    zoom: 18,
    marker: false,
    minLength: 1,
    delayType: 100,
    autoType: false,
    tooltipLimit: 10,
    tipAutoSubmit: true,
    autoCollapse: false,
    textErr: '找不到這隻寵物',
    textCancel: '取消',
    textPlaceholder: '搜尋寵物名稱...'
});

fetch('/api', { method: 'POST' })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('API request failed: ' + response.status);
        }
        return response.json();
    })
    .then(function (map_data) {
        for (var i = 0; i < map_data.length; i++) {
            var title = map_data[i].Name;
            var selfIcon = L.divIcon({
                className: 'my-div-icon',
                iconSize: [50, 50],
                html: '<img class="circle_img" src="' + map_data[i].Picture + '" style="border: 3px solid ' + map_data[i].Color + '" />'
            });
            var marker = L.marker(new L.LatLng(map_data[i].Latitude, map_data[i].Longitude), {
                title: title,
                icon: selfIcon
            }).setBouncingOptions({
                bounceHeight: 20,
                exclusive: true
            }).on('click', function () {
                this.bounce(3);
            }).addTo(markers);

            var content = title + "<br>Latitude: " + map_data[i].Latitude + "<br>Longitude: " + map_data[i].Longitude;
            marker.bindPopup(content, {
                maxWidth: 600
            });

            markers.addLayer(marker);
            markerList.push(marker);
        }

        controlSearch.on('search:locationfound', function (e) {
            if (e.layer._popup) {
                var index = markerList.map(function (m) {
                    return m.options.title;
                }).indexOf(e.text);
                var m = markerList[index];
                markers.zoomToShowLayer(m, function () {
                    m.openPopup();
                    m.bounce(3);
                });
            }
        });

        map.addControl(controlSearch);
        // IME (中文輸入法) commits don't fire keyup; bind input to trigger search
        controlSearch._input.addEventListener('input', function (e) {
            controlSearch._handleKeypress(e);
        });
        map.addLayer(markers);

        L.control.locate({
            position: 'topright',
            strings: {
                title: "Show me where I am, yo!",
                popup: "i am here"
            },
            drawCircle: true,
            showPopup: true
        }).addTo(map);

        L.control.zoom({
            position: 'topright'
        }).addTo(map);
    })
    .catch(function (err) {
        console.error(err);
    });
