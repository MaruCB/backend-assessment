from unittest.mock import MagicMock, patch

from backend_assessment.data_exporter import DataExporter
from backend_assessment.models import Company, User


@patch("backend_assessment.data_exporter.os")
def test_create_file_if_directory_does_not_exists(mock_os: MagicMock) -> None:
    mock_os.path.exists = MagicMock(return_value=True)
    mock_os.mkdir = MagicMock(return_value=None)

    DataExporter().create_file()
    mock_os.path.exists.assert_called()
    mock_os.mkdir.assert_not_called()


@patch("backend_assessment.data_exporter.os")
def test_create_file_if_directory_exists(mock_os: MagicMock) -> None:
    mock_os.path.exists = MagicMock(return_value=False)
    mock_os.mkdir = MagicMock(return_value=None)

    DataExporter().create_file()
    mock_os.path.exists.assert_called()
    mock_os.mkdir.assert_called()


@patch("backend_assessment.data_exporter.os")
@patch("backend_assessment.data_exporter.open")
def test_write_file(mock_open: MagicMock, mock_os: MagicMock) -> None:

    user_list = []
    new_user = User(
        company_id=1,
        surname="ras",
        location="London",
        forename="Ras",
        date_of_birth="1990/01/31",
    )
    new_user.full_name = "Ras ras"
    company = Company(
        headquarters="Nellie", id=1, name="Wonderland", industry="Fluffyness"
    )
    new_user.company = company
    user_list.append(new_user)

    # Mock create file.exist
    mock_os.path.exists.side_effect = [True, False]
    mock_os.remove = MagicMock(return_value=True)
    mock_open = MagicMock(return_value=None)
    mock_open.write = MagicMock(return_value=None)

    DataExporter().write_file(user_list)
    mock_os.path.exists.called_count(2)
    mock_os.remove.assert_not_called()


@patch("backend_assessment.data_exporter.os")
@patch("backend_assessment.data_exporter.open")
def test_write_file_remove(mock_open: MagicMock, mock_os: MagicMock) -> None:

    user_list = []
    new_user = User(
        company_id=1,
        surname="ras",
        location="London",
        forename="Ras",
        date_of_birth="1990/01/31",
    )
    new_user.full_name = "Ras ras"
    company = Company(
        headquarters="Wonderlan", id=1, name="Nellie", industry="Fluffyness"
    )
    new_user.company = company
    user_list.append(new_user)

    # Mock create file.exist
    mock_os.path.exists.side_effect = [True, True]
    mock_os.remove = MagicMock(return_value=True)
    mock_open = MagicMock(return_value=None)
    mock_open.write = MagicMock(return_value=None)

    DataExporter().write_file(user_list)
    mock_os.path.exists.called_count(2)
    mock_os.remove.assert_called()
