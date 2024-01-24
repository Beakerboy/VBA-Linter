from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from typing import TypeVar


T = TypeVar('T', bound='TrailingWhitespace')


class TrailingWhitespace(TokenSequenceMismatch):
    def __init__(self: T) -> None:
        message = "Trailing whitespace"
        super().__init__(
            "305",
            [vbaLexer.NEWLINE, vbaLexer.WS, vbaLexer.NEWLINE],
            1,
            message
        )
