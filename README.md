# Backend Assessment

The code in this repo is the solution we came up with to a technical challenge designed by LifeWorks, for an Associate Product Engineer position. The main goal was to learn how to solve software development problems holistically, implementing Object Oriented Programing [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming), [UnitTest](https://docs.python-guide.org/writing/tests/), [GitHub Actions](https://docs.github.com/en/actions), among other technologies.
The solution is written in Python.

# Installation
In order to run our app locally, you will need to have already installed Python. Check it with:
```
% python --version
```
If no version number is returned, please install [Python](https://python.land/installing-python) before continuing.

## Dependencies

You'll also need to run all dependencies of the project with:
```
poetry install
poetry run my-script
```
You can find more information about Poetry [here](https://python-poetry.org/docs/basic-usage/#using-poetry-run).


# Tasks

The original three tasks were based around user and company JSON data stored in the `./assets/user.json` and `./assets/company.json` files. These files have not been modified, so anyone looking at this repo can give it a go to resolve the tasks. We created a new `./output/output.json` file showing the modified JSON data.

### Task 1

The first was about transforming the user collection so each record would contain a new `full_name` field as shown in the example below.

```js
{
    "forename": "Jane",
    "surname": "Smith",
    "full_name": "Jane Smith",
    "date_of_birth": "2001/10/12",
    "location": "London",
    "company_id": 3
}
```

### Task 2

The second task was about transforming the user collection so it would only contain records where the user is 30 years in age or older.

### Task 3

The third task was about transforming the user collection so each record would contain a new `company` field which contains the company object and replaces the `company_id` field as shown in the example below.

This should be based on the relationship defined by the `company_id` field contained in the user collection and the `id` field contained in the company collection.

```js
{
    "forename": "Jane",
    "surname": "Smith",
    "date_of_birth": "2001/10/12",
    "location": "London",
    "company": {
        "id": 3,
        "name": "Solomon Sisters Bank",
        "headquarters": "London",
        "industry": "Finance"
    }
}
```

## How to Contribute
Feel free to fork our repo and create a pull request with any changes you'd like to see us incorporate. We're open to suggestions :)

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request


## Acknowledgments and Contact
[Maria Casado](https://github.com/MaruCB)
[Rasmus Fangel](https://github.com/RasmusFangel)
