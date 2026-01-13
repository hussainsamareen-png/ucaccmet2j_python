# .3 intercity rains

import json
import csv

with open ('precipitation.json', encoding = 'utf-8') as file:
    data = json.load(file)

print(data)
print(type(data))
results_dic ={}
with open('stations.csv', mode = 'r') as csvfile:
    per_line = csvfile.readline()
    #information = csv.DictReader(csvfile)
    for lines in csvfile:
        line_strip = lines.strip()
        lines_split = line_strip.split(",")
        print(lines_split)
        city = lines_split[0]
        state = lines_split[1]
        station = lines_split[2]
        
        results_dic[city] = {
            'state': state,
            'station': station
            
        }
print(results_dic)

#filter by station
for city in results_dic:
    city_dict = results_dic[city]
    station = city_dict['station']
    city_data = []
    total_yearly = 0
    for element in data:
        if element['station'] == station:
            city_data.append(element)
        total_yearly += element["value"]
            # print(city_data)

# monthly precipitation
    total_monthly_precipitation = {}
    for measurement in city_data:
        month_split = measurement["date"].split("-")
        month = month_split[1]
        if month not in total_monthly_precipitation:
            total_monthly_precipitation[month] = measurement["value"]
        else:
            total_monthly_precipitation[month] += measurement["value"]
    # print(total_monthly_precipitation)

   
    
    #2.1 total yearly percipitation 
    total_yearly_precipitation = 0
    for measurement in city_data:
            total_yearly_precipitation += measurement['value']
    # print(total_yearly_precipitation)

    # 2.2 relative monthly precipitation.
    relative_monthly_precipitation = {}
    for month in total_monthly_precipitation:
        relative_monthly_precipitation[month] = total_monthly_precipitation[month]/ total_yearly_precipitation
        
    # print(relative_monthly_precipitation)


    #relative yearly precipitation
    for city in results_dic:
        relative_yearly_precipitation = total_yearly_precipitation / total_yearly
    print(relative_yearly_precipitation)


# results = {'station': station,
#                         'total_monthly_precipitation': total_monthly_precipitation,
#                         'total_yearly precipitation': total_yearly_precipitation,
#                         'relative_monthly_precipitation': relative_monthly_precipitation,
#                         }
# print(results)










    




# stations = []
# stations = set() ### distinct operation
# for element in data:
#     if element['station'] not in stations:
#         stations.add(element['station'])
# print(stations)






    
    
    

   
    
















