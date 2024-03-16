import re
from typing import Type, TypeVar
from antlr4 import CommonTokenStream

T = TypeVar('T', bound='RuleBase')


class RuleBase:
    def __init__(self: T) -> None:
        # The name or code of the error
        self._rule_name = ""

        # The error message
        self._message = ''

        # True if the error can be correctex
        self._fixable = False

        # Enum?
        self.severity = 'E'

    def set_rule_name(self: T, value: str) -> None:
        self._rule_name = value

    def get_rule_name(self: T) -> str:
        return self._rule_name

    @property
    def severity(self: T) -> str:
        return self._severity

    @severity.setter
    def severity(self: T, value: str) -> None:
        self._severity = value

    def test(self: T, token_stream: CommonTokenStream) -> list:
        return []

    def create_message(self: T, data: tuple) -> str:
        message = self._message
        if message == '' and len(data) == 4:
            message = "%s"
        return (":%s:%s: " + self._severity + "%s " + message) % data

    @classmethod
    def split_nl(cls: Type[T], nl: str) -> list:
        """
        split a newline token into separate line-end characters.
        """
        num = len(nl)
        i = 0
        result = []
        while i < num:
            if num >= 2 and nl[i:i+2] == '\r\n':
                result.append('\r\n')
                i += 2
            else:
                result.append(nl[i:i+1])
                i += 1
        return result

    @classmethod
    def text_matches(cls: Type[T], pattern: str, name: str) -> bool:
        match = re.match(pattern, name)
        if match:
            return True
        return False
