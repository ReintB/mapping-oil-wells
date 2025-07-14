import csv
import json

def dms_to_decimal(direction, degrees, minutes, seconds):
    decimal = degrees + minutes / 60 + seconds / 3600

    # if direction in ['S', 'W']:
    #     decimal *= -1

    return decimal

coordinates = [
    {
        "latitude":  ("N", 0, 50, 0),
        "longitude": ("E", 117, 49, 42)
    },
    {
        "latitude":  ("N", 0, 50, 0),
        "longitude": ("E", 117, 44, 0)
    },
    {
        "latitude":  ("N", 1, 16, 42),
        "longitude": ("E", 117, 44, 0)
    },
    {
        "latitude":  ("N", 0, 30, 0),
        "longitude": ("E", 117, 49, 42)
    },
    {
        "latitude":  ("N", 0, 30, 0),
        "longitude": ("E", 118, 11, 42)
    },
    {
        "latitude":  ("N", 0, 40, 0),
        "longitude": ("E", 118, 12, 0)
    },
    {
        "latitude":  ("N", 0, 40, 0),
        "longitude": ("E", 118, 50, 0)
    },
    {
        "latitude":  ("N", 1, 0, 0),
        "longitude": ("E", 118, 50, 0)
    },
    {
        "latitude":  ("N", 1, 1, 48),
        "longitude": ("E", 118, 11, 24)
    },
]

converted = []
for coord in coordinates:
    lat_dir, lat_deg, lat_min, lat_sec = coord["latitude"]
    lon_dir, lon_deg, lon_min, lon_sec = coord["longitude"]

    lat_decimal = dms_to_decimal(lat_dir, lat_deg, lat_min, lat_sec)
    lon_decimal = dms_to_decimal(lon_dir, lon_deg, lon_min, lon_sec)

    converted.append((lat_decimal, lon_decimal))

print("Hasil Konversi & Link Google Maps:")
for i, (lat, lon) in enumerate(converted, start=1):
    url = f"https://www.google.com/maps?q={lat},{lon}"
    print(f"{i}. Latitude: {lat:.6f}, Longitude: {lon:.6f} → {url}")

with open('coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'Latitude', 'Longitude'])
    for i, (lat, lon) in enumerate(converted, start=1):
        writer.writerow([i, lat, lon])
print("\nFile 'coordinates.csv' berhasil dibuat.")

geojson_data = {
    "type": "FeatureCollection",
    "features": []
}

for i, (lat, lon) in enumerate(converted, start=1):
    feature = {
        "type": "Feature",
        "properties": {
            "id": i
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat]  # GeoJSON = [longitude, latitude]
        }
    }
    geojson_data["features"].append(feature)

with open('coordinates.geojson', 'w') as file:
    json.dump(geojson_data, file, indent=2)
print("File 'coordinates.geojson' berhasil dibuat.")