from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_after_base import TokenAfterBase
from typing import TypeVar


T = TypeVar('T', bound='E201')


class E201(TokenAfterBase):
    def __init__(self: T) -> None:
        self._rule_name = "E201"
        self._token_find = vbaLexer.LPAREN
        self._token_bad = vbaLexer.WS
        self._message = "Unexpected whitespace after '('"
