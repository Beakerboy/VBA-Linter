from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W501')


class W501(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W501"
        self._max_len = 79

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if token.column > self._max_len:
                    output.append((token.line, self._max_len, "W501", token.column))
        return output

    def create_message(self: T, data: tuple) -> str:
        template = ":%s:%s: %s line too long (%s > %s characters)"
        return template % (data[0], data[1], self._rule_name, data[3], self._max_len)
