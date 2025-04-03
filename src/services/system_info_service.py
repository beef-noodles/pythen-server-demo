import logging

from src.models.case import SystemInfo
from src.repositories.system_info_repository import SystemInfoRepository


logger = logging.getLogger(__name__)


class SystemInfoService:
    def __init__(self, system_info_repository: SystemInfoRepository):
        self.system_info_repository = system_info_repository

    def get_latest_one_by_case_id(self, case_id: str):
        return self.system_info_repository.get_latest_one_by_case_id(case_id)

    def create(self, case_id: str, new_system_info: SystemInfo):
        return self.system_info_repository.create(case_id, new_system_info)
