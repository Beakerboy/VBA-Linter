from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W191')


class W191(RuleBase):
    """
    report if a non-blank line has a mix of chars
    in the leading whitespace
    """
    def __init__(self: T) -> None:
        self._rule_name = 'W191'
        self._message = "indentation contains tabs"

    def test(self: T, lexer: vbaLexer) -> list:
        tokens = lexer.getAllTokens()
        output: list[tuple] = []
        for token in tokens:
            if token.type == vbaLexer.WS and token.column == 0:
                # if next token exists and is not NEWLINE
                # should the scope be checked to decide if this
                # is unexpeced indentation?
                i = 1
                for char in token.text:
                    if char == '\t':
                        line = token.line
                        rule = self._rule_name
                        output.append((line, i, rule))
        return output
