from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='KeywordCaps')


class KeywordCaps(RuleBase):
    """
    report if a keyword is not capitalized
    """
    def __init__(self: T) -> None:
        self._severity = 'E'
        self._rule_name = '220'
        self._message = "Keyword not capitalized"

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        # todo: add check for 'VB_Name' type keywords.
        pattern = "^[A-Za-z][A-Za-z]+$"
        text = token.text
        type = token.type
        generics = [vbaLexer.IDENTIFIER, vbaLexer.BASE, vbaLexer.VERSION]
        if type not in generics and KeywordCaps.text_matches(pattern, text):
            pattern = "^[A-Z][a-z]+$"
            if not KeywordCaps.text_matches(pattern, text):
                line = token.line
                column = token.column
                rule = self._rule_name
                output = [(line, column + 1, rule)]
        return output
