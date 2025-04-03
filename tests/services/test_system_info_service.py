import unittest
from unittest.mock import MagicMock
from src.services.system_info_service import SystemInfoService
from tests.fixtures import Fixture


class TestSystemInfoService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock()
        self.service = SystemInfoService(self.mock_repository)

    def test_get_latest_one_by_case_id(self):
        case_id = "test_case_id"
        expected_result = [
            {"id": Fixture.UUID1, "name": "System1"},
            {"id": Fixture.UUID2, "name": "System2"},
        ]
        self.mock_repository.get_latest_one_by_case_id.return_value = expected_result

        result = self.service.get_latest_one_by_case_id(case_id)

        self.mock_repository.get_latest_one_by_case_id.assert_called_once_with(case_id)
        self.assertEqual(result, expected_result)

    def test_create(self):
        case_id = "test_case_id"
        data = {"name": "New System"}
        expected_result = {"id": Fixture.UUID1, "name": "New System"}
        self.mock_repository.create.return_value = expected_result

        result = self.service.create(case_id, data)

        self.mock_repository.create.assert_called_once_with(case_id, data)
        self.assertEqual(result, expected_result)
