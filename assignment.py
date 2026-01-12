import json

with open ('precipitation.json', encoding = 'utf-8') as file:
    content = json.load(file)
    print(content)

