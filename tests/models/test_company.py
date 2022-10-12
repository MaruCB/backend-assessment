from backend_assesment.models import Company


# Notice that we test the to_json function on Company here
def test_company_to_json() -> None:
    test_company = Company(
        id=1,
        name="Razzmatazz industries",
        headquarters="London",
        industry="Software Development",
    )

    expected_result = {
        "id": 1,
        "name": "Razzmatazz industries",
        "headquarters": "Denmark",
        "industry": "Software Development"
    }

    assert expected_result == test_company.to_json()
