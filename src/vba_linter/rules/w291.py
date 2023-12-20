from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='W291')


class W291(TokenBeforeBase):
    def __init__(self: T) -> None:
        message = "trailing whitespace"
        super().__init__("W291", vbaLexer.WS, vbaLexer.NEWLINE, message)

    def create_message(self: T, data: tuple) -> str:
        message = self._message
        if data[1] == 1:
            data = (data[0], 1, "W293")
            message = "blank line contains whitespace"
        return (":%s:%s: %s " + message) % data
