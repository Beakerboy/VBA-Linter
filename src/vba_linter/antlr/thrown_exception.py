from antlr4.error.Errors import ParseCancellationException
from typing import TypeVar


T = TypeVar('T', bound='ThrownException')


class ThrownException(ParseCancellationException):

    def __init__(self: T, message: str):
        super().__init__(message)
        self.msg = ''
        self.line = 0
        self.column = 0
