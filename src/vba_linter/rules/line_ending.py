from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='LineEnding')


class LineEnding(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "W500"
        self._line_ending = '\r\n'
        self._message = 'incorrect line ending'

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        if token.type == vbaLexer.NEWLINE:
            newline_list = RuleBase.split_nl(token.text)
            num_nl = len(newline_list)
            for i in range(num_nl):
                if newline_list[i] != self._line_ending:
                    column = token.column if i == 0 else 0
                    output.append((token.line + i, column, "W500"))
        return output
