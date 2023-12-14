from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_after_base import TokenAfterBase
from typing import TypeVar


T = TypeVar('T', bound='E201')


class E201(TokenAfterBase):
    def __init__(self: T) -> None:
        message = "Whitespace after '('"
        super().__init__("E201", vbaLexer.LPAREN, vbaLexer.WS, message)
