import logging

from src.models.case import SystemEvaluationResult
from src.repositories.system_evaluation_result_repository import (
    SystemEvaluationResultRepository,
)


logger = logging.getLogger(__name__)


class SystemEvaluationResultService:
    def __init__(
        self, system_evaluation_result_repository: SystemEvaluationResultRepository
    ):
        self.system_evaluation_result_repository = system_evaluation_result_repository

    def get_latest_one_by_system_info_id(self, system_info_id: str, tag: str = None):
        return (
            self.system_evaluation_result_repository.get_latest_one_by_system_info_id_and_filter(
                system_info_id, tag
            )
        )

    def create(
        self, system_info_id: str, new_system_evaluation_result: SystemEvaluationResult
    ):
        return self.system_evaluation_result_repository.create(
            system_info_id, new_system_evaluation_result
        )
