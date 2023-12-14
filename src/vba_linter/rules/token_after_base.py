from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='TokenAfterBase')


class TokenAfterBase(TokenBeforeBase):

    def __init__(self: T, first: int, second: int) -> None:
        self._rule_name = ""
        self._token_first = first
        self._token_second = second
        self._message = ""

    def test(self: T, tokens: list) -> list:
        temp = super().test(tokens)
        output: list[tuple] = []
        for err in temp:
            output.append((err[0], err[1] + 1, err[2]))
        return output
