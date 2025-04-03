import logging
from flask import Blueprint
from datetime import datetime

from .dto.health_dto import health_dto

health_bp = Blueprint("health", __name__)
logger = logging.getLogger(__name__)

@health_bp.route("", methods=["GET"])
def health_check():
    health_data = {
        "status": "UP",
        "datetime": datetime.now()
    }
    response = health_dto.to_response(health_data)

    return response
