import json
from typing import List
from models import Company, User


class DataImporter():
    USER_PATH = "./assets/user.json" 
    COMPANY_PATH = "./assets/company.json"

    def read_companies_data(self) -> List[Company]:
        companies_list = []
        with open(self.COMPANY_PATH) as f:
            company_data = json.load(f)

        for company in company_data: 
            c = Company(
                id=company["id"], name=company["name"], headquarters=company["headquarters"], industry=company["industry"]
            )
            companies_list.append(c)

        return companies_list

    def read_users_data(self) -> List[User]:
        users_list = []

        with open(self.USER_PATH) as f:
            user_data = json.load(f)

        for user in user_data:
            the_company = None
            for company in self.read_companies_data():
                if user["company_id"] == company.id:
                    the_company = company
            u = User(
                forename=user["forename"],
                surname=user["surname"],
                date_of_birth=user["date_of_birth"],
                location=user["location"],
                company=the_company,
            )
            users_list.append(u)
        return users_list

