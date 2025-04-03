import unittest
from unittest.mock import MagicMock

from src.models.case import SystemEvaluationResult
from src.services.system_evaluation_result_service import SystemEvaluationResultService
from tests.fixtures import Fixture


class TestSystemEvaluationResultService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock()
        self.service = SystemEvaluationResultService(self.mock_repository)

    def test_get_latest_one_by_system_info_id(self):
        expected_result = SystemEvaluationResult(id=Fixture.UUID1)
        self.mock_repository.get_latest_one_by_system_info_id_and_filter.return_value = expected_result

        result = self.service.get_latest_one_by_system_info_id(Fixture.UUID1)

        self.assertEqual(result, expected_result)

    def test_should_be_none_when_get_latest_one_by_system_info_id_given_no_result_from_repo(
        self,
    ):
        self.mock_repository.get_latest_one_by_system_info_id_and_filter.return_value = None

        result = self.service.get_latest_one_by_system_info_id(Fixture.UUID1)

        self.assertIsNone(result)

    def test_create(self):
        system_info_id = Fixture.UUID1
        data = {"tag": "New System"}
        expected_result = SystemEvaluationResult(id=Fixture.UUID1, tag="New System")
        self.mock_repository.create.return_value = expected_result

        result = self.service.create(system_info_id, data)

        self.mock_repository.create.assert_called_once_with(system_info_id, data)
        self.assertEqual(result.tag, expected_result.tag)
        self.assertIsNotNone(result.id)
