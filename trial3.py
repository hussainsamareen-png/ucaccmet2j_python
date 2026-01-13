# import json

# with open ('precipitation.json', encoding = 'utf-8') as file:
#     data = json.load(file)
# print(data)
# print(type(data))

# results ={}

# stations = set() ### distinct operation
# for element in data:
#     if element['station'] not in stations:
#         stations.add(element['station'])


# #station filter
# for station in stations:
#     station_filter = []
#     for element in data:
#         if element['station'] == station:
#             station_filter.append(element)
#         # print(station_filter)
#     total_monthly_precipitation = {}
#     month = 1
#     while month <= 12:
#         total_monthly_precipitation[month] = 0
#         for measurement in station_filter:
#             if measurement["date"].startswith(f"2010-0{month}"):
#                 total_monthly_precipitation[month] += measurement['value']
#             month += 1
#     print(f'Monthy precipitation in {station} is {total_monthly_precipitation}')

#     # total yearly precipitation

#     total_yearly_precipitation = 0
#     for measurement in station_filter:
#         total_yearly_precipitation += measurement['value']
#     print(f'Total yearly precipitation in {station} is {total_yearly_precipitation}')

#     # Relative monthly precipitation

#     relative_monthly_precipitation = {}
#     for  month in total_monthly_precipitation:
#         relative_monthly_precipitation[month] = total_monthly_precipitation[month]/ total_yearly_precipitation
#     print((f'Relative yearly precipitation in {station} is {relative_monthly_precipitation}'))

#     # Relative yearly precipitation per station

#     results[station] = {'station': station,
#                         'total_monthly_precipitation': total_monthly_precipitation,
#                         'total_yearly precipitation': total_yearly_precipitation,
#                         'relative_monthly_precipitation': relative_monthly_precipitation,
#                         }
#     with open('results.json', 'w', encoding='utf-8') as file:
#         json.dump(results, file, indent=4) 
    







    




