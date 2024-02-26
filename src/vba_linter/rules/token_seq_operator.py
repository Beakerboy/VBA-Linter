from vba_linter.rules.token_sequence_base import TokenSequenceBase
from antlr4_vba.vbaLexer import vbaLexer
from typing import List, Tuple, TypeVar, Union


T = TypeVar('T', bound='TokenSequenceOperator')


class TokenSequenceOperator(TokenSequenceBase):
    """
    Create an error if the stream matches a given sequence
    of token types. we assume the target token is at index
    1, and indicaye which is the wildcard.
    If the sequence has whitespace in the 1st index, and
    the wildcard is not one of the allowed types, produce
    an error.
    """
    def __init__(self: T, name: str,
                 seq: Union[List[int], Tuple[List[int], ...]],
                 wildcard: int, msg: str) -> None:
        super().__init__(name, seq, 1, msg)
        self._wildcard = wildcard

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        Unless the previous token is in the list.
        """
        symbols = [
            vbaLexer.AND, vbaLexer.IF,
            vbaLexer.MOD, vbaLexer.NOT, vbaLexer.OR,
            vbaLexer.WHILE,
            vbaLexer.ASSIGN, vbaLexer.DIV, vbaLexer.EQ,
            vbaLexer.GEQ, vbaLexer.GT, vbaLexer.LEQ,
            vbaLexer.LT, vbaLexer.MINUS, vbaLexer.MINUS_EQ,
            vbaLexer.MULT, vbaLexer.NEQ, vbaLexer.PLUS,
            vbaLexer.PLUS_EQ, vbaLexer.POW,
            vbaLexer.STRINGLITERAL
        ]
        token = sequence[self._wildcard]
        if sequence[1:] == signature[1:]:
            if token not in symbols:
                return True
        return False
