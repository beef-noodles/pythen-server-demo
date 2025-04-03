import unittest

from pydantic import ValidationError
from src.routes.schemas.system_evaluation_result_schema import (
    SystemEvaluationResultCreateSchema,
    SystemEvaluationResultQuerySchema,
)

mock_tag = "tag"


class TestSytemEvaluationResultSchema(unittest.TestCase):
    mock_data = {"key": "value"}
    mock_summary = "summary"

    def test_should_pass_given_valid_data(self):
        result = SystemEvaluationResultCreateSchema(
            tag=mock_tag, data=self.mock_data, summary=self.mock_summary
        )

        self.assertEqual(result.tag, mock_tag)
        self.assertEqual(result.data, self.mock_data)
        self.assertEqual(result.summary, self.mock_summary)

    def test_should_pass_given_paramsters_are_none(self):
        result = SystemEvaluationResultCreateSchema()

        self.assertEqual(result.tag, None)
        self.assertEqual(result.data, None)
        self.assertEqual(result.summary, None)

    def test_should_pass_given_more_field(self):
        with self.assertRaises(ValidationError):
            SystemEvaluationResultCreateSchema(
                tag=mock_tag,
                data=self.mock_data,
                summary=self.mock_summary,
                more="more",
            )


class TestSystemEvaluationResultQuerySchema(unittest.TestCase):
    def test_should_pass_given_tag_is_none(self):
        result = SystemEvaluationResultQuerySchema()

        self.assertEqual(result.tag, None)

    def test_should_pass_given_tag_is_not_none(self):
        result = SystemEvaluationResultQuerySchema(tag=mock_tag)

        self.assertEqual(result.tag, mock_tag)

    def test_should_fail_given_more_field(self):
        with self.assertRaises(ValidationError):
            SystemEvaluationResultQuerySchema(more="more")
