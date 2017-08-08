import json

with open('data.json','r') as fh:
    dictionary = json.load(fh)

print(dictionary['rain'])


