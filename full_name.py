import json

with open('assets/user.json') as f:
   data = json.load(f)

for i in data['empl_details']:
    full_name = f"{i['forename']} {i['surname']}"
    i["full_name"] = full_name
    print(json.dumps(i))