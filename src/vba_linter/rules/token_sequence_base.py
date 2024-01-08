from antlr4 import CommonTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import List, Type, TypeVar


T = TypeVar('T', bound='TokenSequenceBase')


class TokenSequenceBase(RuleBase):
    """
    Create an error if the stream mathes a given sequence
    of token types.
    """
    def __init__(self: T, name: str,
                 sequence: list, target: int,
                 message: str) -> None:
        self._rule_name = name
        self._sequence = sequence

        # The element who's position is reported
        self._target = target + 1
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        tokens: list = []
        for i in range(len(self._sequence)):
            tokens.append(ts.LA(i + 1))
        if TokenSequenceBase.match(tokens, self._sequence):
            token = ts.LT(self._target)
            line = token.line
            column = token.column
            name = self._rule_name
            output = [(line, column + 1, name)]
        return output

    @classmethod
    def match(cls: Type[T], sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        for i in range(len(signature)):
            if sequence[i] != signature[i]:
                return False
        return True
