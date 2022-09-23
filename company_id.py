import json

with open('assets/company.json') as f:
   company_data = json.load(f)


with open('assets/user.json') as f:
   user_data = json.load(f)
#    print(user_data)

for user in user_data['empl_details']:
    companyId = user['company_id']
    for company in company_data:
        if companyId == company['id']:
            user['company'] = company
            user.pop("company_id")
            print(json.dumps(user))
        
