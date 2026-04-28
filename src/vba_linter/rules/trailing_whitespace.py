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

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        result = True
        for i in range(len(sequence)):
            if i == self._target - 2:
                result = result and sequence[i] != signature[i]
            else:
                result = result and sequence[i] == signature[i]
        return result
