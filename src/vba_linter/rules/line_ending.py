from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='LineEnding')


class LineEnding(RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "400"
        self._line_ending = '\r\n'
        self._allowed_blank_lines = 2
        self._message = 'incorrect line ending'
        self._fixable = True

    def test(self: T, ts: CommonTokenStream) -> list:
        name = self._rule_name
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        if token.type == vbaLexer.NEWLINE:
            newline_list = RuleBase.split_nl(token.text)
            num_nl = len(newline_list)
            for i in range(num_nl):
                if newline_list[i] != self._line_ending:
                    column = token.column if i == 0 else 0
                    output.append((token.line + i, column, name))
            new_text = self._line_ending * num_nl
            token.text = new_text
        return output
