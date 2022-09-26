class Company:
    id: int
    name: str
    headquaters: str
    industry: str

    def __init__(self, id: int, name: str, headquaters: str, industry: str):
        self.id = id
        self.name = name
        self.headquaters =  headquaters
        self.industry = industry


class User:
    forename: str
    surname: str
    full_name: str
    date_of_birth: str
    location: str
    company: Company # Is it?

    def __init__(self, forename: str, surname: str, full_name: str, date_of_birth: str, location: str):
        self.forename = forename
        self.surname = surname
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.location = location


