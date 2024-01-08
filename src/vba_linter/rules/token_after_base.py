from antlr4 import CommonTokenStream
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import List, TypeVar


T = TypeVar('T', bound='TokenAfterBase')


class TokenAfterBase(TokenBeforeBase):

    def __init__(self: T, name: str,
                 first: int, second: int,
                 message: str) -> None:
        self._rule_name = name
        self._token_first = first
        self._token_second = second
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        temp = super().test(ts)
        output: List[tuple] = []
        for err in temp:
            output.append((err[0], err[1] + 1, err[2]))
        return output
