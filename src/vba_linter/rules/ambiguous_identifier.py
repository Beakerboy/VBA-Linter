from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='AmbiguousIdentifier')


class AmbiguousIdentifier(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "E741"
        self._names = ['l', 'O', 'I']
        self._message = 'ambiguous variable name'
        self._type = vbaLexer.IDENTIFIER

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        if token.type == self._type:
            output = self._match_action(token)
        return output

    def _match_action(self: T, token: Token) -> list:
        if token.text in self._names:
            return [(token.line, token.column, self._rule_name)]
