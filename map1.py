import folium as fl
import pandas as pd

def colour_producer(el):
    
    if(el == '' or ""):
        return "black"
    elif int(el) <500000:
        return "green"
    elif 1000<= int(el)<=5000000:
        return "orange"
    else:
         return "red"


# data = pd.read_json("a-detailed-version.json")

ds = pd.read_json("in.json")

inpop = list(ds["population"])
latitude = list(ds["lat"])
longitude = list(ds["lng"])

# location= list(data["LOCATION"])
elevation= list(ds["city"])
map = fl.Map(location = [23.25,77.4167],zoom_start =4.5,tiles ="Stamen Terrain")

fgv =fl.FeatureGroup(name ="Indian Cities")

for ip,el,lt,lon in zip(inpop,elevation,latitude,longitude):
     fgv.add_child(fl.CircleMarker(location=[lt,lon],popup= str(el)+" Population : "+str(ip)+" ",fill_color=colour_producer(ip),color = 'grey',fill_opacity=0.7))
    

fgp = fl.FeatureGroup(name="Population")
fgp.add_child(fl.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read(),style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005'] <20000000 else 'red'}))   




map.add_child(fgp)
map.add_child(fgv)
map.add_child(fl.LayerControl())

map.save("Map.html")
