from typing import Any, Dict, Optional
from datetime import datetime


class Company:
    id: int
    name: str
    headquarters: str
    industry: str

    def __init__(self, id: int, name: str, headquarters: str, industry: str) -> None:
        self.id = id
        self.name = name
        self.headquarters = headquarters
        self.industry = industry

    def to_json(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "headquarters": self.headquarters,
            "industry": self.industry,
        }


class User:
    forename: str
    surname: str
    full_name: Optional[str]
    date_of_birth: str
    location: str
    company_id: int
    company: Optional[Company]

    def __init__(
        self,
        forename: str,
        surname: str,
        date_of_birth: str,
        location: str,
        company_id: int,
    ) -> None:
        self.forename = forename
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.location = location
        self.company_id = company_id

    def to_json(self) -> Dict[str, Optional[str]]:
        json_output = {
            "forename": self.forename,
            "surname": self.surname,
            "full_name": self.full_name,
            "date_of_birth": self.date_of_birth,
            "location": self.location,
        }

        if self.company:
            json_output.update({"company": self.company.to_json()})

        return json_output

    @property  #  This means that it gets treated as a field like you've defined on line 22
    # That way we can call it like this: user.age (attribute) rather than user.age() which is a functional call
    def age(self) -> int:
        birthdate = datetime.strptime(self.date_of_birth, "%Y/%m/%d").date()
        today = datetime.today()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age
