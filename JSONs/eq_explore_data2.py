import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

"""making a list of all magnitudes"""
filename = '/home/gato/SCRIPTS_001/JSONs/4.5_day.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

## map the terremotos

data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Los Terremotos")
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='terremotos.html')