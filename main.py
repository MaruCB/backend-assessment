import os
import json
from typing import List
from models import Company, User
from datetime import datetime

PATH = 'output/output.json'


def get_company() -> List[Company]:

   with open('assets/company.json') as f:
      company_data = json.load(f)

   companies_list = []
   for company in company_data:
      c = Company(id=company["id"],name=company["name"], headquarters=company["headquarters"], industry=company["industry"] )
      companies_list.append(c)
   
   return companies_list


def get_user() -> List[User]:

   with open('assets/user.json') as f:
      user_data = json.load(f)

   users_list = []   
   for user in user_data:
      the_company = None

      for company in get_company():
         if user['company_id'] == company.id:
            the_company = company

      u = User(forename=user["forename"], surname=user["surname"], date_of_birth=user["date_of_birth"], location=user["location"], company=the_company)

      birthdate = datetime.strptime(u.date_of_birth, '%Y/%m/%d').date()
      today = datetime.today()    
      age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
      if age >= 30:
         users_list.append(u)
   
   return users_list


dir = os.path.join("output")
if not os.path.exists(dir):
    os.mkdir(dir)

json_list = []

for user in get_user():
   json_list.append(user.to_json())

   if os.path.exists(PATH):
      os.remove(PATH)

with open(PATH, 'w') as f:
   json.dump(json_list, f, indent=4)
