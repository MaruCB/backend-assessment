import json
from typing import List
from backend_assesment.models import Company, User


class DataImporter:
    USER_PATH = "./assets/user.json"
    COMPANY_PATH = "./assets/company.json"

    def read_companies_data(self) -> List[Company]:
        companies_list = []
        with open(self.COMPANY_PATH) as f:
            company_data = json.load(f)

        for company in company_data:
            c = Company(
                id=company["id"],
                name=company["name"],
                headquarters=company["headquarters"],
                industry=company["industry"],
            )
            companies_list.append(c)

        return companies_list

    def read_users_data(self) -> List[User]:
        users_list = []

        with open(self.USER_PATH) as f:
            user_data = json.load(f)

        for user in user_data:

            u = User(
                forename=user["forename"],
                surname=user["surname"],
                date_of_birth=user["date_of_birth"],
                location=user["location"],
                company_id=user["company_id"],
            )
            users_list.append(u)
        return users_list
