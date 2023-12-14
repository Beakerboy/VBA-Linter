from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='W200')


class W200(TokenBeforeBase):
    def __init__(self: T) -> None:
        super().__init__(vbaLexer.NEWLINE, vbaLexer.WS)
        self._rule_name = "W200"
        self._message = "Unexpected whitespace at the end of the line"
