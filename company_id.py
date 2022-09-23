import json

with open('assets/company.json') as f:
   company_data = json.load(f)

with open('assets/user.json') as f:
   user_data = json.load(f)

for user in user_data['empl_details']:
    company_id = user['company_id']
    for company in company_data:
        if company_id == company['id']:
            user['company'] = company
            user.pop("company_id")
            print(json.dumps(user))