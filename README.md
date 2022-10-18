# Backend Assessment

This application is written in Python. It was initially created to learn how to solve software development problems holistically, implementing Object Oriented Programing [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming), [UnitTest](https://docs.python-guide.org/writing/tests/), [GitHub Actions](https://docs.github.com/en/actions),

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


## Tips and Advice

Each of the tasks are relatively simple in that they represent common problems which have well documented solutions.
So our main focus will not be assessing the specifics of how you solve each task.

To complete this assessment well you should consider carefully what steps you'd need to take to make this repo and code
production and team ready. What features would the code and repo require so it can be safely pushed to production
and another developer can easily edit and extend it.

## Tasks

The three tasks are based around user and company JSON data stored in the `./assets/user.json`
and `./assets/company.json` files. Please review each collection of data before working on the tasks.

Be aware we do not care how you output the results of the data transformations, that is entirely up to you.

### Task 1

Transform the user collection so each record contains a new `full_name` field as shown in the example below.

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

Transform the user collection so it only contains records where the user is 30 years in age or older.

### Task 3

Transform the user collection so each record contains a new `company` field which contains the company object
and replaces the `company_id` field as shown in the example below.

This should be based on the relationship defined by the `company_id` field contained in the user collection
and the `id` field contained in the company collection.

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
