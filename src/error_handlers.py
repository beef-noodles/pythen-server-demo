import logging
from flask import jsonify
from http import HTTPStatus
from werkzeug.exceptions import HTTPException
from src.exceptions.api_exceptions import APIException
import traceback

logger = logging.getLogger(__name__)

def _log_error_stack_trace(error):
    logger.error("".join(traceback.format_exception(None, error, error.__traceback__)))

def register_error_handlers(app):
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        _log_error_stack_trace(error)
        response = {"message": error.message}
        return jsonify(response), error.status_code

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        _log_error_stack_trace(error)
        response = {"message": error.description}
        return jsonify(response), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        _log_error_stack_trace(error)
        response = {
            "message": "An unexpected error occurred",
        }
        return jsonify(response), HTTPStatus.INTERNAL_SERVER_ERROR
