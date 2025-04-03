from src import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, JSON, TEXT


class Case(db.Model):
    __tablename__ = "cases"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    active = db.Column(db.Boolean, default=True, nullable=False)
    name = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Case {self.id}>"


class SystemInfo(db.Model):
    __tablename__ = "system_infos"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    case_id = db.Column(UUID(as_uuid=True), db.ForeignKey("cases.id"), nullable=False)
    data = db.Column(JSON, nullable=True)
    meta_data = db.Column(JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<system_infos {self.id}>"


class SystemEvaluationResult(db.Model):
    __tablename__ = "system_evaluations_results"

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    system_info_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("system_infos.id"), nullable=False
    )
    tag = db.Column(db.String(256), nullable=True)
    data = db.Column(JSON, nullable=True)
    summary = db.Column(TEXT, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<system_evaluations_results {self.id}>"
