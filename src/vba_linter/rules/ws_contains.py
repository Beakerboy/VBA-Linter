from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='WsContains')


class WsContains(RuleBase):
    """
    report if a non-blank line has a mix of chars
    in the leading whitespace
    """
    def __init__(self: T) -> None:
        self._severity = 'E'
        self._rule_name = '100'
        self._message = "Whitespace contains tabs"
        self._bad_char = '\t'

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        if token.type == vbaLexer.WS:
            # if next token exists and is not NEWLINE
            # should the scope be checked to decide if this
            # is unexpeced indentation?
            i = 1
            for char in token.text:
                if char == self._bad_char:
                    line = token.line
                    if token.column == 0:
                        rule = "100:405"
                    output = [(line, i, rule)]
        return output
