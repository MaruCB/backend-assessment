from unittest.mock import MagicMock, patch


@patch("backend_assessment.data_importer.json")
@patch("backend_assessment.data_exporter.os")
@patch("backend_assessment.data_exporter.open")
def test_main(
    mock_open: MagicMock, mock_os: MagicMock, mock_data_importer_json: MagicMock
) -> None:
    # Execute main
    test_user_data = [
        {
            "forename": "Maria",
            "surname": "Casado",
            "date_of_birth": "1988/02/13",
            "location": "London",
            "company_id": 1,
        }
    ]

    test_companies_data = [
        {
            "id": 1,
            "name": "Head Journal",
            "headquarters": "San Francisco",
            "industry": "Tech",
        }
    ]
    # Patch read_user_data
    mock_data_importer_json.load.side_effect = [test_user_data, test_companies_data]
    # mock_data_exporter.create_file = MagicMock(return_value=None)
    # Path write_file
    mock_os.path.exists.side_effect = [True, False]
    # mock_os.path.exist = MagicMock(return_value= True)
    mock_open = MagicMock(return_value=None)  # noqa: F841
