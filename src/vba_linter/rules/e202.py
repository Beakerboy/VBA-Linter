from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='E202')


class E202(TokenBeforeBase):
    def __init__(self: T) -> None:
        self._rule_name = "E202"
        self._token_find = vbaLexer.RPAREN
        self._token_bad = vbaLexer.WS

    def create_message(self: T, data: tuple) -> str:
        output = TokenBeforeBase.create_message(self, data)
        return output + "Unexpected whitespace bedore ')'"
