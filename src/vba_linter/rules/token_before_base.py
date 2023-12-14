from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


class TokenBeforeBase(RuleBase):
    def __init__(self: T, name: str,
                 first: int, second: int,
                 message: str) -> None:
        self._rule_name = name
        self._token_second = second
        self._token_first = first
        self._message = message

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            if token.type == self._token_second:
                first = self._token_first
                if not (prev_tok is None) and prev_tok.type == first:
                    line = token.line
                    column = token.column
                    name = self._rule_name
                    output.append((line, column, name))
            prev_tok = token
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + self._message
