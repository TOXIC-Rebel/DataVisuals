import json
import requests
from plotly.graph_objs import Layout
from plotly import offline

def get_data_from_json_file():
    """Get settings from a eq_link.json
     where we store the link to a JSON file with data."""
    with open('data/eq_link.json') as file:
        return json.load(file)

def get_questions_data_by_requests():
    """Requesting json with data from the internet."""
    request_url = get_data_from_json_file()['eq']
    response = requests.get(request_url)
    return response.json()

all_eq_data = get_questions_data_by_requests()

readable_file = 'data/readeble_eq.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Plotting data on a map.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

