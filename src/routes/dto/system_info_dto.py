from datetime import datetime
from flask import jsonify
from typing import TypedDict

from src.routes.schemas.system_info_schema import SystemInfoCreateModel
from src.utils.common import format_datetime


from .base import DTOMapper
from src.models.case import SystemInfo


class SystemInfoResponse(TypedDict):
    id: str
    data: bool
    caseId: str
    createdAt: datetime
    updatedAt: datetime


class SystemInfoDTO(DTOMapper[SystemInfo, SystemInfoResponse]):
    def _to_response(self, entity: SystemInfo) -> SystemInfoResponse:
        system_info_response = {
            "id": entity.id,
            "data": entity.data,
            "caseId": entity.case_id,
            "createdAt": format_datetime(entity.created_at),
            "updatedAt": format_datetime(entity.updated_at),
        }
        return system_info_response

    def to_response(self, entity: SystemInfo) -> SystemInfoResponse:
        return jsonify(self._to_response(entity))

    def to_creation_response(self, entity: SystemInfo) -> SystemInfoResponse:
        return jsonify({"id": entity.id})

    def from_request(self, request_data: SystemInfoCreateModel) -> SystemInfo:
        return SystemInfo(data=request_data.data, meta_data=request_data.metadata)


system_info_dto = SystemInfoDTO()
