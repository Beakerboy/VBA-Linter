from typing import TypeVar
from vba_linter.rules.rule_base import Rulebase


class RuleStub(RuleBase):

    def __init__(self: T) -> None:
        self._output: list[tuple] = []
        self._message = ''

    def set_message(self: T, message: str) -> None:
        self._message = message

    def set_output(self:T, output: list) -> None:
        self._output = output

    def test(self: T, tokens: list) -> list:
        return self._output

    def create_message(self: T, data: tuple) -> str:
        return self._message
