import json
from datetime import datetime

with open('assets/user.json') as f:
   data = json.load(f)

for i in data:
    date_string = f"{i['date_of_birth']}"
    birthdate = datetime.strptime(date_string, '%Y/%m/%d').date()
    today = datetime.today()    
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    if age >= 30:
        print(i)