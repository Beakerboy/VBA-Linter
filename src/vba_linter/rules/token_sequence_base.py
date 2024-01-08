from antlr4 import CommonTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


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
        self._target = target
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        tokens: List[Token] = []
        for i in range(len(self._sequence):
            tokens.append(ts.LA(i + 1))
        pos = TokenSequenceBase.compare(tokens, self._sequence)
        if pos > 0:
            token = ts.LT(pos)
            line = token.line
            column = token.column
            name = self._rule_name
            output = [(line, column, name)]
        return output

    @classmethod
    def compare(cls: Type[T], sequence: list, signature: list) -> int:
        """
        Compare the two lists. Provide the index of the firat non-matching
        element.
        """
        for i in range(len(signature)):
            if sequence[i] != signature[i]:
                return i + 1
            return 0
