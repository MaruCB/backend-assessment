from data_importer import DataImporter
from data_exporter import DataExporter

data_importer = DataImporter()
# 1. Read users data
users_data = data_importer.read_users_data()

# 2. Iterate over that data and add full name to users
for user in users_data:
    full_name = f"{user.forename} {user.surname}"
    user.full_name = full_name

# 3. Only process users over 30yo
over_thirty = []
for user in users_data:
    if user.age >= 30:
        over_thirty.append(user)

# 4. Add companies to users with matching ids, delete company_id in users
companies_data = data_importer.read_companies_data()

for user in over_thirty:
    for company in companies_data:
        if user.company_id == company.id:
            user.company = company

# 5. Write the file
DataExporter().write_file(over_thirty)
