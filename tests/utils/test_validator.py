import unittest
from unittest.mock import patch, MagicMock
from pydantic import BaseModel

from src.utils.validator import validate_json_data, validate_request_body
from src.exceptions.api_exceptions import ValidationException


class TestModel(BaseModel):
    field: str


class TestValidator(unittest.TestCase):
    @patch("src.utils.validator._validate_model")
    def test_validate_request_body_success(self, mock_validate_model):
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"field": "value"}
        mock_validate_model.return_value = TestModel(field="value")

        result = validate_request_body(TestModel, mock_request)

        self.assertEqual(result.field, "value")
        mock_validate_model.assert_called_once_with(TestModel, field="value")

    @patch("src.utils.validator._validate_model")
    def test_validate_request_body_validation_error(self, mock_validate_model):
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"field": "value"}
        mock_validate_model.side_effect = ValidationException(
            [{"loc": ("field",), "msg": "error", "type": "type_error"}]
        )

        with self.assertRaises(ValidationException):
            validate_request_body(TestModel, mock_request)
        mock_validate_model.assert_called_once_with(TestModel, field="value")

    def test_validate_json_data_success(self):
        valid_json = '{"field": "value"}'
        result = validate_json_data(valid_json)
        self.assertEqual(result, {"field": "value"})

    def test_validate_json_data_invalid_json(self):
        invalid_json = '{"field": "value"'
        with self.assertRaises(ValidationException):
            validate_json_data(invalid_json)
