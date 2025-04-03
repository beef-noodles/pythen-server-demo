import unittest
from pydantic import ValidationError
from src.routes.schemas.system_info_schema import SystemInfoCreateModel
from tests.fixtures import Fixture


class TestSystemInfoCreateModel(unittest.TestCase):
    mock_data = {"test": "test", "id": Fixture.UUID1}
    mock_arry_data = [mock_data, {"more": {"more": True}}]

    def test_system_info_create_model_success(self):
        model = SystemInfoCreateModel(data=self.mock_data, metadata=self.mock_data)

        self.assertEqual(model.data, self.mock_data)
        self.assertEqual(model.metadata, self.mock_data)

    def test_system_info_create_model_success_given_list_mock_data(self):
        model = SystemInfoCreateModel(data=self.mock_data, metadata=self.mock_arry_data)

        self.assertEqual(model.data, self.mock_data)
        self.assertEqual(model.metadata, self.mock_arry_data)

    def test_system_info_create_model_optional_fields(self):
        model = SystemInfoCreateModel()

        self.assertIsNone(model.data)
        self.assertIsNone(model.metadata)

    def test_system_info_create_model_extra_fields(self):
        with self.assertRaises(ValidationError):
            SystemInfoCreateModel(
                data="some data", metadata="some metadata", extra_field="not allowed"
            )
