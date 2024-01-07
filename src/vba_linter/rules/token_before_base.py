from antlr4 import BufferedTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


class TokenBeforeBase(RuleBase):
    """
    """
    def __init__(self: T, name: str,
                 first: int, second: int,
                 message: str) -> None:
        self._rule_name = name
        self._token_second = second
        self._token_first = first
        self._message = message

    def test(self: T, ts: BufferedTokenStream) -> list:
        output: List[tuple] = []
        if ts.p < 2:
            return output
        token = ts.LT(1)
        if (token == self._token_second and
                ts.LT(-1) == self._token_first):
            line = token.line
            column = token.column
            name = self._rule_name
            output.append((line, column, name))
        return output
