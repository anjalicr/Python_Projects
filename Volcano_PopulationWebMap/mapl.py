import folium
import pandas as pd
#base layer, marker layer and polygon layer
data = pd.read_csv(r"Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name= list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

html = """
Volcano Name: <br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location = [38.2,-99.1] , zoom_start= 5, tiles="CartoDB positron ")
fg_vol = folium.FeatureGroup(name="Volcanoes") #Feature group is used to keep your code organized as well as to add multiple childs(Layered controles Feature) to one map object

fg_pop = folium.FeatureGroup(name="Population")
fg_pop.add_child(folium.GeoJson(data = open('world.json' , 'r' , encoding = 'utf-8-sig').read(),
style_function=lambda x: {'color':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) #x represents features here from json file

fg_vol = folium.FeatureGroup(name="Volcanoes") #Feature group is used to keep your code organized as well as to add multiple childs(Layered controles Feature) to one map object

for lt, ln, el, name in zip(lat , lon , elev, name) :

    iframe = folium.IFrame(html=html % (name, name ,el) , width=200, height=100)
    fg_vol.add_child(folium.CircleMarker(location=[lt,ln],radius = 5, popup = folium.Popup(iframe) , #icon = folium.Icon(color=color_producer(el) )))
    fill_color=color_producer(el) , color = 'grey' , fill_opacity = 0.7))


map.add_child(fg_pop)
map.add_child(fg_vol)


map.add_child(folium.LayerControl())

map.save("Map_html_popup_advanced.html")
