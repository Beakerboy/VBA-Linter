from vba_linter.rules.token_sequence_base import TokenSequenceBase
from antlr4_vba.vbaLexer import vbaLexer
from typing import TypeVar


T = TypeVar('T', bound='TokenSequenceOperator')


class TokenSequenceOperator(TokenSequenceBase):
    """
    Create an error if the stream matches a given sequence
    of token types.
    """
    def __init__(name, seq, target, msg) -> None:
        super().__init__(name, seq, 2, msg)
        self._wildcard = target

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
        token = sequence[self._wildcard]
        if sequence == signature:
            if token not in symbols:
                return True
