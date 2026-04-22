<?php 
include 'config/koneksi.php'; 
?>
<!DOCTYPE html>
<html>
<head>
    <title>Peta Persebaran DBD Manado</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
    <style>
        #map { height: 500px; }
    </style>
</head>
<body>

<h2>Peta Persebaran DBD Kota Manado</h2>
<div id="map"></div>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>

var map = L.map('map').setView([1.4748, 124.8421], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'OpenStreetMap'
}).addTo(map);

<?php
$query = mysqli_query($conn, "SELECT * FROM kasus_dbd");
while ($data = mysqli_fetch_array($query)) {
?>
L.marker([<?= $data['latitude']; ?>, <?= $data['longitude']; ?>])
.addTo(map)
.bindPopup(`
    <b>Wilayah:</b> <?= $data['wilayah']; ?><br>
    <b>Kasus:</b> <?= $data['jumlah_kasus']; ?><br>
    <b>Tanggal:</b> <?= $data['tanggal']; ?>
`);
<?php 
} 
?>
</script>
</body>
</html>