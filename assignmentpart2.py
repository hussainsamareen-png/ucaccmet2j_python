import json

with open ('precipitation.json', encoding = 'utf-8') as file:
    data = json.load(file)
print(data)
print(type(data))

results = {}

stations = set() ### distinct operation
for element in data:
    stations.add(element['station'])
print(stations)

#filtering by station
for station in stations:
    station_data = []










