from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from typing import TypeVar


T = TypeVar('T', bound='TrailingWhitespace')


class TrailingWhitespace(TokenSequenceMismatch):
    def __init__(self: T) -> None:
        message = "trailing whitespace"
        super().__init__(
            "305",
            [vbaLexer.NEWLINE, vbaLexer.WS, vbaLexer.NEWLINE],
            1,
            message
        )

    def create_message(self: T, data: tuple) -> str:
        if data[1] == 1:
            data = (data[0], 1, "310")
            self._message = "Blank line contains whitespace"
        else:
            self._message = "trailing whitespace"
        return super().create_message(data)
