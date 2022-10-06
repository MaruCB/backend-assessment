from unittest.mock import MagicMock, patch
from backend_assesment.data_importer import DataImporter
from backend_assesment.models import User
# from freezegun import freeze_time
# import datetime


@patch("backend_assesment.data_importer.json")
@patch("backend_assesment.data_exporter.os")
@patch("backend_assesment.data_exporter.open")
def test_main(mock_open: MagicMock, mock_os: MagicMock, mock_data_importer_json: MagicMock) -> None: 
    # Execute main
    test_user_data = [{
        "forename": "Maria",
        "surname": "Casado",
        "date_of_birth": "1988/02/13",
        "location": "London",
        "company_id": 1
    }]

    test_companies_data = [{
        "id": 1,
        "name": "Head Journal",
        "headquarters": "San Francisco",
        "industry": "Tech"
    }]
    # Patch read_user_data
    mock_data_importer_json.load.side_effect = [test_user_data, test_companies_data]
    # mock_data_exporter.create_file = MagicMock(return_value=None)
    # Path write_file
    mock_os.path.exists.side_effect = [True, False]
    # mock_os.path.exist = MagicMock(return_value= True)
    mock_open = MagicMock(return_value=None)

    from backend_assesment import main



# @path("backend_assesment.data_exporter.create_file")

# @path("backend_assesment.data_exporter.os")

# def test_user_full_name(mock_data_importer_json: MagicMock) -> None:
#     mock_data_importer_json.load = MagicMock(return_value=test_user_data)

#     assert users[0].full_name == "Maria Casado"


# def test_user_over_thirty(mock_data_importer_datetime: MagicMock) -> None:
#     users = DataImporter().read_users_data()
#     birthday = users[0].date_of_birth
#     # birthday_to_int = birthday.replace("/", " ")
#     # test_birthday = int(birthday_to_int)
    
#     @freeze_time("01/01/1991")
#     def test_today():
#         datetime.today() == datetime.today(1/1/1991)


