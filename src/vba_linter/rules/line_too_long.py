from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='LineTooLong')


class LineTooLong(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "W501"
        self._max_len = 79
        self._message = ("line too long (%s > " +
                         str(self._max_len) + " characters)")

    def test(self: T, ts: CommonTokenStream) -> List:
        output: List[tuple] = []
        token = ts.LT(1)
        if token.type == vbaLexer.NEWLINE:
            if token.column > self._max_len:
                line = token.line
                column = token.column
                pos = self._max_len + 1
                output.append((line, pos, "W501", column))
        return output
