from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TrailingWhitespace')


class TrailingWhitespace(TokenSequenceBase):
    def __init__(self: T) -> None:
        message = "trailing whitespace"
        super().__init__("305", [vbaLexer.WS, vbaLexer.NEWLINE], 0, message)

    def create_message(self: T, data: tuple) -> str:
        message = self._message
        if data[1] == 1:
            data = (data[0], 1, "310")
            self._message = "Blank line contains whitespace"
        else:
            self._message = "trailing whitespace"
        super().create_message(data)
