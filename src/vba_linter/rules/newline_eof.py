from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='NewlineEof')


class NewlineEof(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "W201"
        self._message = "no newline at end of file"

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        if token.type == Token.EOF and ts.LB(1) != vbaLexer.NEWLINE:
            line = token.line
            column = final_token.column + len(token.text) + 1
            output = [(line, column, "W201")]
        return output
