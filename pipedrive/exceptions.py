class BaseError(Exception):
    def __init__(self, message, response, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.response = response


class BadRequestError(BaseError):
    pass


class UnauthorizedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass


class NotFoundError(BaseError):
    pass


class GoneError(BaseError):
    pass


class UnsupportedMediaTypeError(BaseError):
    pass


class UnprocessableEntityError(BaseError):
    pass


class TooManyRequestsError(BaseError):
    pass


class InternalServerError(BaseError):
    pass


class NotImplementedError(BaseError):
    pass


class ServiceUnavailableError(BaseError):
    pass


class UnknownError(BaseError):
    pass
