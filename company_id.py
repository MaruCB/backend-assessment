import json

with open('assets/company.json') as f:
   company_data = json.load(f)

f.close()

with open('assets/user.json') as f:
   user_data = json.load(f)
#    print(user_data)

for user in user_data['empl_details']:
    for company in company_data:
        if user['company_id'] == company['id']:
            user['company_id'] = company
            user['company_id'] = user.pop('company_id')
            print(json.dumps(user))
        


f.close()