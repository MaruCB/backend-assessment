from backend_assesment.models import User, Company


# Notice that we test the to_json function on User here.
# The test is broken at the moment, can you spot why? Fix it if you can
def test_user_to_json() -> None:
    test_user = User(
        forename="Rasmus",
        surname="Fangel",
        date_of_birth="31-01-1991",
        location="Paddock Wood",
        company_id=1
    )
    test_user.company = Company(
        id=1,
        name="Razzmatazz industries",
        headquarters="Denmark",
        industry="Software Development",
    )

    test_user.full_name = "Rasmus Fangel"

    expected_result = {
        "forename": "Rasmus",
        "surname": "Fangel",
        "full_name": "Rasmus Fangel",
        "date_of_birth": "31-01-1991",
        "location": "Paddock Wood",
        "company": {
            "id": 1,
            "name": "Razzmatazz industries",
            "headquarters": "Denmark",
            "industry": "Software Development",
        },
    }

    assert expected_result == test_user.to_json()


# Here we test the age function
def test_age() -> None:
    test_user = User(
        forename="Rasmus",
        surname="Fangel",
        date_of_birth="1991/01/31",
        location="Paddock Wood",
        company_id=1,
    )

    assert test_user.age == 31


# Here we test the age function
# This does not work, can you tell why?
def test_age_error() -> None:
    test_user = User(
        forename="Rasmus",
        surname="Fangel",
        date_of_birth="1991/01/31",
        location="Paddock Wood",
        company_id=1,
    )

    assert test_user.age == 31
