from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='NewlineEof')


class NewlineEof(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "201"
        self._message = "no newline at end of file"
        self._severity = 'W'

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        if (ts.index > 0 and ts.LA(2) == Token.EOF and
                token.type != vbaLexer.NEWLINE):
            line = token.line
            column = token.column + len(token.text) + 1
            output = [(line, column, "W201")]
        return output
