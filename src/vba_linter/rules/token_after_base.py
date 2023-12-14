from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenAfterBase')


class TokenAfterBase(RuleBase):

    def __init__(self: T, find: int, bad: int) -> None:
        self._rule_name = ""
        self._token_find = find
        self._token_bad = bad
        self._message = ""

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            if token.type == self._token_bad:
                if (not (prev_tok is None) and
                    prev_tok.type == self._token_find):
                        name = self._rule_name
                        column = token.column + 1
                    output.append((token.line, column, name))
            prev_tok = token
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + self._message
