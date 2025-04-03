from datetime import datetime
from flask import jsonify
from typing import TypedDict

from src.utils.common import format_datetime


from .base import DTOMapper
from src.models.case import Case


class CaseResponse(TypedDict):
    id: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    isActive: bool


class CaseDTO(DTOMapper[Case, CaseResponse]):
    def _to_response(self, entity: Case) -> CaseResponse:
        return {
            "id": entity.id,
            "name": entity.name,
            "createdAt": format_datetime(entity.created_at),
            "updatedAt": format_datetime(entity.updated_at),
            "isActive": entity.active,
        }

    def to_response(self, entity: Case) -> CaseResponse:
        return jsonify(self._to_response(entity))

    def to_response_list(self, entities: list[Case]) -> list[CaseResponse]:
        return jsonify([self._to_response(entity) for entity in entities])


case_dto = CaseDTO()
