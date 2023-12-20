from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W201')


class W201(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "W201"
        self._message = "no newline at end of file"

    def test(self: T, lexer: vbaLexer) -> list:
        tokens = lexer.getAllTokens()
        output: list[tuple] = []
        if len(tokens) == 0:
            return output
        final_token = tokens[-1]
        if final_token.type != vbaLexer.NEWLINE:
            line = final_token.line
            column = final_token.column + len(final_token.text) + 1
            output = [(line, column, "W201")]
        return output
