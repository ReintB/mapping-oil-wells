import folium
from geopy.distance import geodesic

converted = [
    (0.833333, 117.828333),
    (0.833333, 117.733333),
    (1.278333, 117.733333),
    (0.500000, 117.828333),
    (0.500000, 118.195000),
    (0.666667, 118.200000),
    (0.666667, 118.833333),
    (1.000000, 118.833333),
    (1.030000, 118.190000),
]

center_lat, center_lon = converted[0]

m = folium.Map(location=[center_lat, center_lon], zoom_start=8)

for i, (lat, lon) in enumerate(converted, start=1):
    folium.Marker(
        location=[lat, lon],
        popup=f"Titik {i}<br>Lat: {lat:.6f}<br>Lon: {lon:.6f}",
        tooltip=f"Titik {i}"
    ).add_to(m)

for i in range(len(converted) - 1):
    start = converted[i]
    end = converted[i + 1]
    distance_km = geodesic(start, end).kilometers

    folium.PolyLine(
        locations=[start, end],
        color='blue',
        weight=3,
        opacity=0.7,
        tooltip=f"Jarak Titik {i+1} → {i+2}: {distance_km:.2f} km",
        popup=f"{distance_km:.2f} km"
    ).add_to(m)

    mid_lat = (start[0] + end[0]) / 2
    mid_lon = (start[1] + end[1]) / 2

    folium.map.Marker(
        [mid_lat, mid_lon],
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 12px; color: darkred;">{distance_km:.2f} km →</div>"""
        )
    ).add_to(m)

m.save("map_with_distance_and_labels.html")
print("Buka 'map_with_distance_and_labels.html' di browser.")