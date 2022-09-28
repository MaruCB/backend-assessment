class Company:
    id: int
    name: str
    headquarters: str
    industry: str

    def __init__(self, id: int, name: str, headquarters: str, industry: str):  # missing return type
        self.id = id
        self.name = name
        self.headquarters = headquarters
        self.industry = industry

    def to_json(self):  # missing return type
        return {
            'id': self.id,
            'name': self.name,
            'headquarters': self.headquarters,
            'industry': self.industry
        }


class User:
    forename: str
    surname: str
    full_name: str
    date_of_birth: str
    location: str
    company: Company

    def __init__(self, forename: str, surname: str, date_of_birth: str, location: str, company: Company):  # Missing return type
        self.forename = forename
        self.surname = surname
        self.full_name = f"{forename} {surname}"
        self.date_of_birth = date_of_birth
        self.location = location
        self.company = company

    # def is_over_thirty(self) -> bool: (bool is True or False)
        # if self.date_of_birth > 30 years:
            # return True
        #else:
            # return False

    def to_json(self):  # missing return type
        return {
            'forename': self.forename,
            'surname': self.surname,
            'full_name': self.full_name,
            'date_of_birth': self.date_of_birth,
            'location': self.location,
            'company': self.company.to_json()
        }
