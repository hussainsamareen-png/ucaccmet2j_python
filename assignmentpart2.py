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
        
        results_dic[lines_split[0]] = {
            'state': lines_split[1],
            'station': lines_split[2]
            
        }
print(results_dic)



    




# stations = []
# stations = set() ### distinct operation
# for element in data:
#     if element['station'] not in stations:
#         stations.add(element['station'])
# print(stations)






    
    
    

   
    
















