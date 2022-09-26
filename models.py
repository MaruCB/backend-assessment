

class User:

    # forename: str
    # surname: str
    # full_name: str
    # date_of_birth: str
    # location: str
    # company: dict # Is it?

    def __init__(self, forename, surname, full_name, date_of_birth, location):
        self.forename: forename
        self.surname: surname
        self.full_name: full_name
        self.date_of_birth: date_of_birth
        self.location: location
        # self.company: ?? 

class Company:
    def __init__(self, id, name, headquaters, industry):
        self.id: id
        self.name: name
        self.headquaters: headquaters
        self.industry: industry


