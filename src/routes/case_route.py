import logging
from http import HTTPStatus
from flask import Blueprint, request
from src import auth
from src.repositories.system_evaluation_result_repository import (
    SystemEvaluationResultRepository,
)
from src.repositories.system_info_repository import SystemInfoRepository
from src.routes.dto.system_evaluation_result_dto import system_evaluation_result_dto
from src.routes.dto.system_info_dto import system_info_dto
from src.routes.schemas.system_evaluation_result_schema import (
    SystemEvaluationResultCreateSchema,
    SystemEvaluationResultQuerySchema,
)
from src.routes.schemas.system_info_schema import SystemInfoCreateModel
from src.services.system_evaluation_result_service import SystemEvaluationResultService
from src.services.system_info_service import SystemInfoService
from src.services.case_service import CaseService
from src.repositories.case_repository import CaseRepository
from src.utils.validator import validate_request_body, validate_request_query_paramter
from .dto.case_dto import case_dto
from src.exceptions.api_exceptions import (
    OperationException,
    ResourceNotFoundException,
)
from functools import wraps
from src.routes.schemas.case_schema import (
    CaseCreateModel,
    CaseUpdateModel,
)

case_bp = Blueprint("cases", __name__)

case_service = CaseService(CaseRepository())
system_info_service = SystemInfoService(SystemInfoRepository())
system_evaluation_result_service = SystemEvaluationResultService(
    SystemEvaluationResultRepository()
)
logger = logging.getLogger(__name__)


def check_case_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        case_id = kwargs.get("id")
        case = case_service.get_case_by_id(case_id)
        if case is None:
            error_message = f"Not found the case for {case_id}"
            logger.error(error_message)
            raise ResourceNotFoundException(error_message)
        return f(*args, **kwargs)

    return decorated_function


@case_bp.route("", methods=["POST"])
@auth.login_required
def create_case():
    request_body = validate_request_body(CaseCreateModel, request)

    case = case_service.create_case(request_body.name)
    return case_dto.to_response(case), HTTPStatus.CREATED


@case_bp.route("", methods=["GET"])
@auth.login_required
def get_cases():
    cases = case_service.get_all_active_cases()
    return case_dto.to_response_list(cases), HTTPStatus.OK


@case_bp.route("/<uuid:id>", methods=["GET"])
@auth.login_required
@check_case_exists
def get_case_by(id):
    case = case_service.get_case_by_id(id)
    return case_dto.to_response(case), HTTPStatus.OK


@case_bp.route("/<uuid:id>", methods=["PATCH"])
@auth.login_required
@check_case_exists
def update_case_name(id):
    logger.info(f"Start to update case: {id}")
    request_body = validate_request_body(CaseUpdateModel, request)

    new_case = case_service.update_case_name(id, request_body.name)
    logger.info(f"Successfully updated case: {id}, name: {request_body.name}")
    return case_dto.to_response(new_case), HTTPStatus.OK


@case_bp.route("/<uuid:id>", methods=["DELETE"])
@auth.login_required
@check_case_exists
def delete_by_case_id(id):
    logger.info(f"Start to delete case: {id}")
    operation_result = case_service.delete_case(id)
    if operation_result is True:
        logger.info(f"Successfully updated case: {id}")
        return {}, HTTPStatus.OK
    else:
        logger.error(f"Failed to delete case: {id}")
        raise OperationException(f"Failed to delete the case {id}")


@case_bp.route("/<uuid:id>/system-infos/latest", methods=["GET"])
@auth.login_required
@check_case_exists
def get_system_infos(id):
    latest_system_info = system_info_service.get_latest_one_by_case_id(id)
    if latest_system_info is None:
        raise ResourceNotFoundException(
            "Not found the latest system info for the case {id}"
        )
    return system_info_dto.to_response(latest_system_info), HTTPStatus.OK


@case_bp.route("/<uuid:id>/system-infos", methods=["POST"])
@auth.login_required
@check_case_exists
def create_system_info(id):
    logger.info(f"Start to creating system info for case: {id}")
    request_body = validate_request_body(SystemInfoCreateModel, request)
    request_body_dto = system_info_dto.from_request(request_body)

    system_info = system_info_service.create(id, request_body_dto)
    logger.info(
        f"Successfully created system info for case: {id}, system_info: {system_info}"
    )
    return system_info_dto.to_creation_response(system_info), HTTPStatus.CREATED


@case_bp.route(
    "/<uuid:id>/system-infos/<uuid:system_info_id>/evaluation-results", methods=["POST"]
)
@auth.login_required
@check_case_exists
def create_system_evaluation_result(id, system_info_id):
    logger.info(
        f"Start to creating system evaluation result for system info id: {system_info_id}"
    )
    request_body = validate_request_body(SystemEvaluationResultCreateSchema, request)
    request_body_dto = system_evaluation_result_dto.from_request(request_body)

    system_evaluation_result_info = system_evaluation_result_service.create(
        system_info_id, request_body_dto
    )
    logger.info(
        f"Successfully created system info for case: {id}, system_info: {system_evaluation_result_info}"
    )
    return system_evaluation_result_dto.to_creation_response(
        system_evaluation_result_info
    ), HTTPStatus.CREATED


@case_bp.route(
    "/<uuid:id>/system-infos/<uuid:system_info_id>/evaluation-results/latest",
    methods=["GET"],
)
@auth.login_required
@check_case_exists
def get_latest_system_evaluation_result(id, system_info_id):
    logger.info(
        f"Start to creating system evaluation result for system info id: {system_info_id}"
    )
    query = validate_request_query_paramter(SystemEvaluationResultQuerySchema, request)

    latest_system_evaluation_result = (
        system_evaluation_result_service.get_latest_one_by_system_info_id(
            system_info_id, query.tag
        )
    )

    if latest_system_evaluation_result is None:
        raise ResourceNotFoundException(
            f"Not found the latest system evaluation result for the system info {system_info_id}"
        )
    logger.info(
        f"Successfully created system info for case: {id}, system_info: {latest_system_evaluation_result}"
    )
    return system_evaluation_result_dto.to_response(
        latest_system_evaluation_result
    ), HTTPStatus.OK
