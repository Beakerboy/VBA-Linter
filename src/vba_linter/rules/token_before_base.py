from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


class TokenBeforeBase(RuleBase):
    """
    Find a token of the given type, and the optional value.
    If the precious token is of the given type, return the
    line and column of the end of the previous token.
    """
    def __init__(self: T, name: str,
                 find: int, bad: int,
                 message: str) -> None:
        self._rule_name = name
        self._token_find = find
        self._token_bad = bad
        self._message = message
        self._find_value = ""

    def set_find_value(self: T, value: str) -> None:
        self._find_value = value

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            value = token.text if self._find_value == '' else self._find_value
            if token.type == self._token_find and token.text == value:
                bad = self._token_bad
                if not (prev_tok is None) and prev_tok.type == bad:
                    line = token.line
                    column = token.column
                    name = self._rule_name
                    output.append((line, column, name))
            prev_tok = token
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + self._message
