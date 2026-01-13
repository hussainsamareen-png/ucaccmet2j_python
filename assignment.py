import json

with open ('precipitation.json', encoding = 'utf-8') as file:
    data = json.load(file)
print(data)
print(type(data))

results = {}

# 0.3: filtering for seattle

seattle_data = []
for element in data:
    if element['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(element)
# print(seattle_data)

# Percipitaion per month

total_monthly_precipitation = {}
month = 1

while month <= 12:
    total_monthly_precipitation[month] = 0
    for measurement in seattle_data:
        if measurement["date"].startswith(f"2010-0{month}-"):
            total_monthly_precipitation[month] += measurement['value']
        elif measurement["date"].startswith(f"2010-{month}-"):
            total_monthly_precipitation[month] += measurement['value']
    month += 1
total_monthly_precipitation_list = list(total_monthly_precipitation.values())
print(total_monthly_precipitation_list)

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation, file, indent=4) 

#.2.1 total yearly percipitation 
total_yearly_precipitation = 0
for measurement in seattle_data:
    total_yearly_precipitation += measurement['value']

print(f'Total yearly precipitation in Seattle is {total_yearly_precipitation}')

   
# 2.2 relative monthly precipitation.

relative_monthly_precipitation = {}
for  month in total_monthly_precipitation:
    relative_monthly_precipitation[month] = total_monthly_precipitation[month]/ total_yearly_precipitation
relative_monthly_precipitation_list = list(relative_monthly_precipitation.values())
print(f'The relative monthly percipitation in seatle for each month is as follows {relative_monthly_precipitation}')

results = {
    'Seatle':{
        'station': 'GHCND:US1WAKG0038',
        'state': 'WA',
        'total_monthly_precipitatio': total_monthly_precipitation_list,
        'total_yearly_precipitation': total_yearly_precipitation,
        'relative_monthly_precipitation': relative_monthly_precipitation_list
    },
}
                            
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4) 

