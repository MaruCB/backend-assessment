import json
from models import Company, User
from datetime import datetime

with open('assets/user.json') as f:
    user_data = json.load(f)

with open('assets/company.json') as f:
    company_data = json.load(f)

companies_list = []

for company in company_data:
    c = Company(id=company["id"],name=company["name"], headquarters=company["headquarters"], industry=company["industry"] )
    companies_list.append(c)

for company in companies_list:
    print(json.dumps(company.to_json()))

users_list = []

for user in user_data:
    the_company = None

    for company in companies_list:
        if user['company_id'] == company.id:
            the_company = company

    u = User(forename=user["forename"], surname=user["surname"], date_of_birth=user["date_of_birth"], location=user["location"], company=the_company)

    birthdate = datetime.strptime(u.date_of_birth, '%Y/%m/%d').date()
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 30:
        users_list.append(u)

for user in users_list:
    print(json.dumps(user.to_json()))
