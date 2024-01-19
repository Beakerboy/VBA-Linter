from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TokenSequenceOperator')


class TokenSequenceOperator(TokenSequenceBase):
    """
    Create an error if the stream matches a given sequence
    of token types.
    """

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        Unless the previous token is in the list.
        """
        symbols = [
            vbaLexer.ASSIGN, vbaLexer.DIV, vbaLexer.EQ,
            vbaLexer.GEQ, vbaLexer.GT, vbaLexer.LEQ,
            vbaLexer.LT, vbaLexer.MINUS, vbaLexer.MINUS_EQ,
            vbaLexer.PLUS
        ]
        result = True
        for i in range(len(sequence)):
            if i == self._target - 1:
                result = result and sequence[i] != signature[i]
            else:
                result = result and sequence[i] == signature[i]
        return result
