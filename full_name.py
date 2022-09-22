import json

with open('assets/user.json') as f:
   data = json.load(f)

#    print(json.dumps(data, indent=4))

# print(data)

for i in data['empl_details']:
    # print(i['forename'],i['surname'])
    full_name = f"{i['forename']} {i['surname']}"
    # print(full_name)
    i["full_name"] = full_name

    print(json.dumps(i))


f.close()
