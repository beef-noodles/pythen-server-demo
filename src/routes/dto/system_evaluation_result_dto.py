from datetime import datetime
from flask import jsonify
from typing import TypedDict

from src.routes.schemas.system_evaluation_result_schema import (
    SystemEvaluationResultCreateSchema,
)
from src.utils.common import format_datetime


from .base import DTOMapper
from src.models.case import SystemEvaluationResult


class SystemEvaluationResultResponse(TypedDict):
    id: str
    systemInfoId: str
    tag: str
    data: dict
    summary: str
    createdAt: datetime
    updatedAt: datetime


class SystemEvaluationResultDTO(
    DTOMapper[SystemEvaluationResult, SystemEvaluationResultResponse]
):
    def _to_response(
        self, entity: SystemEvaluationResult
    ) -> SystemEvaluationResultResponse:
        system_info_response = {
            "id": entity.id,
            "systemInfoId": entity.system_info_id,
            "tag": entity.tag,
            "summary": entity.summary,
            "data": entity.data,
            "createdAt": format_datetime(entity.created_at),
            "updatedAt": format_datetime(entity.updated_at),
        }
        return system_info_response

    def to_response(
        self, entity: SystemEvaluationResult
    ) -> SystemEvaluationResultResponse:
        return jsonify(self._to_response(entity))

    def to_creation_response(
        self, entity: SystemEvaluationResult
    ) -> SystemEvaluationResultResponse:
        return jsonify({"id": entity.id})

    def from_request(
        self, request_data: SystemEvaluationResultCreateSchema
    ) -> SystemEvaluationResult:
        return SystemEvaluationResult(
            tag=request_data.tag,
            data=request_data.data,
            summary=request_data.summary,
        )


system_evaluation_result_dto = SystemEvaluationResultDTO()
