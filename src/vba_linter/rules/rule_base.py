from typing import Type, TypeVar
from antlr4_vba.vbaLexer import vbaLexer

T = TypeVar('T', bound='RuleBase')


class RuleBase:
    def __init__(self: T) -> None:
        self._rule_name = ""
        self._message = ''

    def get_rule_name(self: T) -> str:
        return self._rule_name

    def test(self: T, lexer: vbaLexer) -> list:
        return []

    def create_message(self: T, data: tuple) -> str:
        return (":%s:%s: %s " + self._message) % data

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
