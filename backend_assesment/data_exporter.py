import os
import json
from datetime import datetime
from typing import List
from backend_assesment.models import User


class DataExporter():
    PATH = "./output/output.json"
    file_name = "output"

    def create_file(self):
        dir = os.path.join(self.file_name)
        if os.path.exists(dir):
            ...
        else:
            os.mkdir(dir)

    def write_file(self, list: List[User]):
        self.create_file()
        date = datetime. now(). strftime("%Y_%m_%d-%I:%M:%S_%p")
        users_json = []
        for user in list:
            users_json.append(user.to_json()) 

        json_output = {'timestamp': date}
        json_output.update({"users": users_json})

        if os.path.exists(self.PATH):
            os.remove(self.PATH)
        with open(self.PATH, "w") as f:
            f.write(json.dumps(json_output, indent=4))
            ...
