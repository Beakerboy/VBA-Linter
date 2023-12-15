from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_between_base import TokenBetweenBase
from typing import TypeVar


T = TypeVar('T', bound='E211')


class E211(TokenBetweenBase):
    def __init__(self: T) -> None:
        super().__init__(
            "E211", vbaLexer.IDENTIFIER, vbaLexer.WS,
            vbaLexer.LPAREN, "whitespace before '('"
        )
