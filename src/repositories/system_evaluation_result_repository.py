import uuid_utils as uuid
from src.extensions import db
from src.models.case import SystemEvaluationResult


class SystemEvaluationResultRepository:
    def __init__(self):
        self.db = db

    def create(
        self, system_info_id: str, new_system_evaluation_result: SystemEvaluationResult
    ):
        system_evaluation_result = SystemEvaluationResult()
        system_evaluation_result.id = str(uuid.uuid7())
        system_evaluation_result.system_info_id = system_info_id
        if new_system_evaluation_result.tag is not None:
            system_evaluation_result.tag = new_system_evaluation_result.tag
        if new_system_evaluation_result.data is not None:
            system_evaluation_result.data = new_system_evaluation_result.data
        if new_system_evaluation_result.summary is not None:
            system_evaluation_result.summary = new_system_evaluation_result.summary
        self.db.session.add(system_evaluation_result)
        self.db.session.commit()
        return system_evaluation_result

    def get_latest_one_by_system_info_id_and_filter(self, system_info_id: str, tag: str = None):
        return (
            self.db.session.query(SystemEvaluationResult)
            .filter(SystemEvaluationResult.system_info_id == system_info_id)
            .filter(SystemEvaluationResult.tag == tag if tag is not None else True)
            .order_by(SystemEvaluationResult.updated_at.desc())
            .first()
        )
