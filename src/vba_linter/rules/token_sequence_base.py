from antlr4 import CommonTokenStream, Token
from vba_linter.rules.rule_base import RuleBase
from typing import List, Tuple, Type, TypeVar, Union


T = TypeVar('T', bound='TokenSequenceBase')


class TokenSequenceBase(RuleBase):
    """
    Create an error if the stream mathes a given sequence
    of token types.
    """
    def __init__(self: T, name: str,
                 sequence: Union[List[int], Tuple[List[int]]], target: int,
                 message: str) -> None:
        """
        if sequence is passed in as a tuple, and the contained lists have 
        different lengths, the shorted list kust be first to prevent
        an early return.
        """
        self._rule_name = name
        self._sequence = sequence

        # The element who's position is reported
        self._target = target + 1
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token_types: list = []
        sequences: Tuple[List[int]]
        if type(self._sequence) == list:
            sequences = (self._sequence)
        else:
            sequences = self._sequence
        for sequence in sequences:
            found_eof = False
            for i in range(len(sequence)):
                if found_eof:
                    return output
                tok_type = ts.LA(i + 1)
                if tok_type == Token.EOF:
                    found_eof = True
                token_types.append(tok_type)
            if TokenSequenceBase.match(token_types, sequence):
                token = ts.LT(self._target)
                output = self._match_action(token)
        return output

    def _match_action(self: T, token: Token) -> list:
        line = token.line
        column = token.column
        name = self._rule_name
        return [(line, column + 1, name)]

    @classmethod
    def match(cls: Type[T], sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        return sequence == signature
