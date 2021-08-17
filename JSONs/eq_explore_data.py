import json

"""exploring the structure of the data
this will read the json and create a readable json
then we do next step"""
filename = '/home/gato/SCRIPTS_001/JSONs/all_hour_2.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file  = '/home/gato/SCRIPTS_001/JSONs/read_eq.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)