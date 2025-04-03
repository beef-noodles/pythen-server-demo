from http import HTTPStatus


class APIException(Exception):
    """Base exception class for API errors"""

    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__()
        self.message = message
        self.status_code = status_code


class ResourceNotFoundException(APIException):
    """Exception raised when a requested resource is not found"""

    def __init__(self, message="Resource not found"):
        super().__init__(message=message, status_code=HTTPStatus.NOT_FOUND)


class ValidationException(APIException):
    """Exception raised when request validation fails"""

    def __init__(self, message="Validation error"):
        super().__init__(message=message, status_code=HTTPStatus.BAD_REQUEST)


class OperationException(APIException):
    def __init__(self, message="Failed to do the operaition"):
        super().__init__(message=message, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
