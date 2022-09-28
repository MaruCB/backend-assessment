import json
from models import Company, User
from datetime import datetime

with open('assets/user.json') as f:
    user_data = json.load(f)

# Suggestion: Move line 9-16 into another file (e.g. data_importer.py) and create a class with an approprate
# classname. Then, in that class, load your data and return it to the main file. Do the same for users.
# Both users and companies lists could be returned from that same file.

# This means that your main.py "script" will only have to add companies to users and keep this from getting too cluttered.
# This is probably the hardest part, so feel free to give me a shout if/when you get stuck :)

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

    # Suggestion; add the logic below to the user class as a function, see my example in models.py.
    # That way, all you have to do is;
    # if user.is_over_thirty():
        # users_list.append(u)

    birthdate = datetime.strptime(u.date_of_birth, '%Y/%m/%d').date()
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 30:
        users_list.append(u)

for user in users_list:
    print(json.dumps(user.to_json()))
