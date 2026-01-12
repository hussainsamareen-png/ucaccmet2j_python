import json

with open ('precipitation.json', encoding = 'utf-8') as file:
    data = json.load(file)
print(data)
print(type(data))

# 0.3: filtering for seattle

seattle_data = []
for element in data:
    if element['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(element)
print(seattle_data)



