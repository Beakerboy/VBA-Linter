from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='E203')


class E203(TokenBeforeBase):
    def __init__(self: T) -> None:
        self._rule_name = "E203"
        self._token_second = vbaLexer.T__0
        self._token_first = vbaLexer.WS
        self._message = "Whitespace before ','"
