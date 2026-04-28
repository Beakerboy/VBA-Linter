from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='IndentContains')


class IndentContains(RuleBase):
    """
    report if a non-blank line has a mix of chars
    in the leading whitespace
    """
    def __init__(self: T) -> None:
        self._severity = 'W'
        self._rule_name = '191'
        self._message = "indentation contains tabs"
        self._bad_char = '\t'

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        if token.type == vbaLexer.WS and token.column == 0:
            # if next token exists and is not NEWLINE
            # should the scope be checked to decide if this
            # is unexpeced indentation?
            i = 1
            for char in token.text:
                if char == self._bad_char:
                    line = token.line
                    rule = self._rule_name
                    output = [(line, i, rule)]
        return output
