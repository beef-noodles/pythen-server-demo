import uuid_utils as uuid
from src.extensions import db
from src.models.case import SystemInfo


class SystemInfoRepository:
    def __init__(self):
        self.db = db

    def create(self, case_id: str, new_system_info: SystemInfo):
        system_info = SystemInfo()
        system_info.id = str(uuid.uuid7())
        system_info.case_id = case_id
        if new_system_info.data is not None:
            system_info.data = new_system_info.data
        if new_system_info.meta_data is not None:
            system_info.meta_data = new_system_info.meta_data
        self.db.session.add(system_info)
        self.db.session.commit()
        return system_info

    def update(self, id: int, updated_info: dict):
        system_info = (
            self.db.session.query(SystemInfo).filter(SystemInfo.id == id).first()
        )
        if system_info:
            for key, value in updated_info.items():
                setattr(system_info, key, value)
            self.db.session.commit()
        return system_info

    def get_latest_one_by_case_id(self, case_id: str):
        return (
            self.db.session.query(SystemInfo)
            .filter(SystemInfo.case_id == case_id)
            .order_by(SystemInfo.updated_at.desc())
            .first()
        )
