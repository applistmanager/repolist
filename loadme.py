import json

with open('core.json') as json_file:
    data = json.load(json_file)
    print(data['repo_file'])
