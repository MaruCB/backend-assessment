from typing import Any
from unittest.mock import MagicMock, patch

from backend_assesment.data_importer import DataImporter


@patch("backend_assesment.data_importer.json")
def test_read_companies_data(mock_data_importer_json: MagicMock) -> None:
    test_data = [
        {"id": 1, "name": "ras", "headquarters": "Denmark", "industry": "Software"}
    ]
    mock_data_importer_json.load = MagicMock(return_value=test_data)

    companies = DataImporter().read_companies_data()

    assert companies[0].id == test_data[0]["id"]
    assert companies[0].name == test_data[0]["name"]
    assert companies[0].industry == test_data[0]["industry"]
    assert companies[0].headquarters == test_data[0]["headquarters"]


@patch("backend_assesment.data_importer.json")
def test_read_users_data(mock_data_importer_json: MagicMock):

    users_test_data = [
        {
            "forename": "Ras",
            "surname": "ras",
            "date_of_birth": "2001/10/12",
            "location": "London",
            "company_id": 1,
        }
    ]

    companies_test_data = [
        {"id": 1, "name": "ras", "headquarters": "Denmark", "industry": "Software"}
    ]

    mock_data_importer_json.load.side_effect = [users_test_data, companies_test_data]

    result = DataImporter().read_users_data()

    assert result[0].forename == users_test_data[0]["forename"]
