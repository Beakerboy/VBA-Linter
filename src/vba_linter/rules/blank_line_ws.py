from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='BlankLineWhitespace')


class BlankLineWhitespace(TokenSequenceBase):
    def __init__(self: T) -> None:
        message = "Blank line contains whitespace"
        super().__init__(
            "310",
            [vbaLexer.NEWLINE, vbaLexer.WS, vbaLexer.NEWLINE],
            1,
            message
        )
        self._severity = 'W'
