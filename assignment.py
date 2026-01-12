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
# print(seattle_data)

# Percipitaion per month

total_monthly_precipitation = {}
month = 1

while month <= 12:
    total_monthly_precipitation[month] = 0
    for measurement in seattle_data:
        if measurement["date"].startswith(f"2010-0{month}"):
            total_monthly_precipitation[month] += measurement['value']
    month += 1
print(total_monthly_precipitation)

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(total_monthly_precipitation, file, indent=4) 






    # for measurement in seattle_data:
    #     mont = measurement['date']


#         if month not in total_monthly_precipitation:
#                 total_monthly_precipitation[month] = 0
#                 total_monthly_precipitation[month] += measurement['value']

# print(total_monthly_precipitation)

#         if measurement["date"].startswith(f'2010-0-{month}'):
#          total_precipitation[measurement] += measurement['value']
# print(total_monthly_precipitation)


