import uuid_utils as uuid

from typing import List, Optional
from src.extensions import db
from src.models.case import Case


class CaseRepository:
    def __init__(self):
        self.db = db

    def get_all_active_cases(self, limit: int = None) -> List[Case]:
        return (
            Case.query.filter_by(active=True)
            .order_by(Case.updated_at.desc())
            .limit(limit)
            .all()
        )

    def get_case_by_id(self, case_id: str) -> Optional[Case]:
        return Case.query.get(case_id)

    def save_case(self, case: Case) -> Case:
        case.id = str(uuid.uuid7())
        self.db.session.add(case)
        self.db.session.commit()
        return case

    def update_name(self, id: str, name: str):
        case = self.get_case_by_id(id)
        case.name = name
        self.db.session.commit()
        return case

    def delete_case(self, case_id: str) -> bool:
        case = self.get_case_by_id(case_id)
        case.active = False
        if case:
            self.db.session.commit()
            return True
        return False
