from antlr4 import CommonTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='TokenBetweenBase')


class TokenBetweenBase(RuleBase):
    def __init__(self: T, name: str,
                 first: int, second: int,
                 third: int, message: str) -> None:
        self._rule_name = name
        self._token_second = second
        self._token_first = first
        self._token_third = third
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        tok1 = ts.LT(-1)
        tok2 = ts.LT(1)
        token = ts.LT(2)
        if (token.type == self._token_third and
                tok1.type == self._token_first and
                tok2.type == self._token_second):
            line = token.line
            column = token.column
            name = self._rule_name
            output = [(line, column, name)]
        return output
