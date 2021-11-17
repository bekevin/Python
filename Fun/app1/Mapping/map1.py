import folium
import pandas

def color_producer(elevation: float) -> str:
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <=3000:
        return "orange"
    else:
        return "red"
    

data = pandas.read_csv("files/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """Volcano name:<br> <a href="https://www.google.com/search?q=Mount %s" target="_blank">%s</a><br> Height: %s m"""


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),color="gray", fill_color=color_producer(el), fill_opacity=0.7))

fg.add_child(folium.GeoJson())

map.add_child(fg)

map.save("Map1.html");

