from flask import jsonify
from typing import TypedDict
from src.utils.common import format_datetime

from .base import DTOMapper

class HealthResponse(TypedDict):
    status: str
    datetime: str

class HealthDTO(DTOMapper[dict, HealthResponse]):
    def to_response(self, entity: dict) -> HealthResponse:
        return jsonify({
            "status": entity["status"],
            "datetime": format_datetime(entity["datetime"])
        })

health_dto = HealthDTO()
