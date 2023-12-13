from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W200')


class W501(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W501"
        self._max_len = 80

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if token.column > self._max_len:
                    output.append((token.line, token.column, "W501"))
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return (output + "Line too long (" + str(data[1]) +
                '>' + str(self._max_len) + ')')
