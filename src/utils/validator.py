import json
import logging
from pydantic import ValidationError

from src.exceptions.api_exceptions import ValidationException

logger = logging.getLogger(__name__)


def _validate_model(model, **kwargs):
    try:
        data = model(**kwargs)
        return data
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise ValidationException(e.errors())


def validate_request_body(model, kwargs):
    return _validate_model(model, **kwargs.get_json())


def validate_request_query_paramter(model, kwargs):
    return _validate_model(model, **kwargs.args)


def validate_json_data(data: str) -> dict:
    try:
        data = json.loads(data)
        return data
    except json.JSONDecodeError as e:
        raise ValidationException(f"Invalid JSON data: {e}")
