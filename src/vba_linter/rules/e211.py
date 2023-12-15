from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_between_base import TokenBetweenBase
from typing import TypeVar


T = TypeVar('T', bound='E211')


class E211(TokenBeforeBase):
    def __init__(self: T) -> None:
        self._rule_name = "E203"
        self._token_first = vbaLexer.FUNCTION
        self._token_second = vbaLexer.WS
        self._token_third = vbaLexer.LPAREN
        self._message = "whitespace before '('"
