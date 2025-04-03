import logging
from typing import List, Optional
from src.models.case import Case
from src.repositories.case_repository import CaseRepository

logger = logging.getLogger(__name__)


class CaseService:
    def __init__(self, case_repository: CaseRepository):
        self.case_repository = case_repository

    def get_all_active_cases(self) -> List[Case]:
        logger.info("Start to get all active cases")
        cases = self.case_repository.get_all_active_cases()
        logger.info(f"Successfully get {len(cases)} active cases")
        return cases

    def get_case_by_id(self, case_id: str) -> Optional[Case]:
        return self.case_repository.get_case_by_id(case_id)

    def create_case(self, name: str) -> Case:
        case = Case()
        case.name = name
        return self.case_repository.save_case(case)

    def update_case_name(self, case_id: str, name: str) -> Case:
        return self.case_repository.update_name(case_id, name)

    def delete_case(self, case_id: str) -> bool:
        return self.case_repository.delete_case(case_id)
