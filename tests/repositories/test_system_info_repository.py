import unittest
from unittest.mock import MagicMock
from src.repositories.system_info_repository import SystemInfoRepository
from src.models.case import SystemInfo
from tests.fixtures import Fixture


class TestSystemInfoRepository(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.repo = SystemInfoRepository()
        self.repo.db = self.db_mock

    def test_create(self):
        data = '{"test":"data","id":"1"}'

        new_system_info = SystemInfo(data=data, metadata=data)

        system_info = SystemInfo()
        system_info.id = "test_id"
        self.db_mock.session.add = MagicMock()
        self.db_mock.session.commit = MagicMock()

        result = self.repo.create(Fixture.UUID1, new_system_info)

        self.db_mock.session.add.assert_called_once()
        self.db_mock.session.commit.assert_called_once()
        self.assertEqual(result.case_id, Fixture.UUID1)
        self.assertEqual(result.data, data)
        self.assertEqual(result.meta_data, None)

    def test_should_create_one_givne_none_data(self):
        new_system_info = SystemInfo(data=None, metadata=None)

        system_info = SystemInfo()
        system_info.id = "test_id"
        self.db_mock.session.add = MagicMock()
        self.db_mock.session.commit = MagicMock()

        result = self.repo.create(Fixture.UUID1, new_system_info)

        self.db_mock.session.add.assert_called_once()
        self.db_mock.session.commit.assert_called_once()
        self.assertEqual(result.case_id, Fixture.UUID1)
        self.assertEqual(result.data, None)
        self.assertEqual(result.meta_data, None)

    def test_update(self):
        id = "test_id"
        updated_info = {"key": "new_value"}
        system_info = SystemInfo()
        self.db_mock.session.query().filter().first.return_value = system_info
        self.db_mock.session.commit = MagicMock()

        result = self.repo.update(id, updated_info)

        self.db_mock.session.commit.assert_called_once()
        self.assertEqual(result.key, "new_value")

    def test_get_latest_one_by_case_id(self):
        case_id = "test_case_id"
        system_info = SystemInfo()
        self.db_mock.session.query().filter().order_by().first.return_value = (
            system_info
        )

        result = self.repo.get_latest_one_by_case_id(case_id)

        self.assertEqual(result, system_info)
