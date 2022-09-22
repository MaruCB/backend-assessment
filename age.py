import json
from datetime import datetime
from operator import truediv

with open('assets/user.json') as f:
   data = json.load(f)
#    print(data)


for i in data['empl_details']:
    date_string = f"{i['date_of_birth']}"
    # print(date_string)
    birthdate = datetime.strptime(date_string, '%Y/%m/%d').date()
    today = datetime.today()    
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if age >= 30:
        print(i)


f.close()
