from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleStub')


class RuleStub(RuleBase):

    def __init__(self: T) -> None:
        self._rule_name = ""
        self._output: list[tuple] = []
        self._message = ''
        self.test_count = 0

    def set_name(self: T, name: str) -> None:
        self._name = name

    def set_message(self: T, message: str) -> None:
        self._message = message

    def set_output(self: T, output: list) -> None:
        self._output = output

    def test(self: T, tokens: list) -> list:
        self.test_count += 1
        return self._output

    def create_message(self: T, data: tuple) -> str:
        return self._message
