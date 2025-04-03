import unittest
from unittest.mock import MagicMock
from src.models.case import SystemEvaluationResult
from src.repositories.system_evaluation_result_repository import (
    SystemEvaluationResultRepository,
)
from tests.fixtures import Fixture


class TestSystemEvaluationResultRepository(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.repo = SystemEvaluationResultRepository()
        self.repo.db = self.db_mock

    def test_should_create_a_record(self):
        new_system_evaluation_result = SystemEvaluationResult(
            tag="tag", data="data", summary="summary"
        )
        system_evaluation_result = SystemEvaluationResult()
        system_evaluation_result.id = Fixture.UUID1
        self.db_mock.session.add = MagicMock()
        self.db_mock.session.commit = MagicMock()
        result = self.repo.create(Fixture.UUID2, new_system_evaluation_result)
        self.db_mock.session.add.assert_called_once()
        self.db_mock.session.commit.assert_called_once()
        self.assertEqual(result.system_info_id, Fixture.UUID2)
        self.assertEqual(result.tag, new_system_evaluation_result.tag)
        self.assertEqual(result.data, new_system_evaluation_result.data)
        self.assertEqual(result.summary, new_system_evaluation_result.summary)

    def test_should_create_a_record_given_None_for_some_fields(self):
        new_system_evaluation_result = SystemEvaluationResult(
            tag=None, data=None, summary=None
        )
        system_evaluation_result = SystemEvaluationResult()
        system_evaluation_result.id = Fixture.UUID1
        self.db_mock.session.add = MagicMock()
        self.db_mock.session.commit = MagicMock()
        result = self.repo.create(Fixture.UUID2, new_system_evaluation_result)
        self.db_mock.session.add.assert_called_once()
        self.db_mock.session.commit.assert_called_once()
        self.assertEqual(result.system_info_id, Fixture.UUID2)
        self.assertEqual(result.tag, new_system_evaluation_result.tag)
        self.assertEqual(result.data, new_system_evaluation_result.data)
        self.assertEqual(result.summary, new_system_evaluation_result.summary)

    def test_should_get_latest_one_by_system_info_id_and_filter(self):
        system_evaluation_result = SystemEvaluationResult()
        system_evaluation_result.id = Fixture.UUID1
        tag = "tag"
        system_evaluation_result.tag = tag
        self.db_mock.session.query.return_value.filter.return_value.filter.return_value.order_by.return_value.first.return_value = system_evaluation_result

        result = self.repo.get_latest_one_by_system_info_id_and_filter(
            Fixture.UUID1, tag
        )

        self.assertEqual(result.id, Fixture.UUID1)
        self.assertEqual(result.tag, tag)

    def test_should_get_latest_one_by_system_info_id_given_no_filter(self):
        system_evaluation_result = SystemEvaluationResult()
        system_evaluation_result.id = Fixture.UUID1
        tag = None
        system_evaluation_result.tag = tag
        self.db_mock.session.query.return_value.filter.return_value.filter.return_value.order_by.return_value.first.return_value = system_evaluation_result

        result = self.repo.get_latest_one_by_system_info_id_and_filter(
            Fixture.UUID1, tag
        )

        self.assertEqual(result.id, Fixture.UUID1)
        self.assertEqual(result.tag, tag)
