from .abc import ABCExceptionFactory
from .code_error import CodeErrorFactory
from .error_handler import ABCErrorHandler, ErrorHandler
from .single_error import SingleError
from .swear_handler import swear

TGAPIError = CodeErrorFactory()


class TottleError(SingleError):
    pass
