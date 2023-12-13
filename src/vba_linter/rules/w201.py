from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W201')


class W201(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W201"

    def test(self: T, tokens: list) -> list:
        final_token = tokens[-1]
        if final_token is None or final_token.type != vbaLexer.NEWLINE:
            line = 1 if final_token is None else final_token.line
            column = 0 if final_token is None else final_token.column
            return [(line, column, "W201")]
          
