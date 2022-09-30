from data_importer import DataImporter
from data_exporter import DataExporter

users_list = []

for user in DataImporter().read_users_data():
    if user.age() >= 30:
        users_list.append(user)

data_exporter = DataExporter()

data_exporter.write_file(list=users_list)
