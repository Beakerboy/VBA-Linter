from antlr4 import CommonTokenStream, Token
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='BlankLineEof')


class BlankLineEof(RuleBase):
    """
    Returns an error if the final line is solely a newline character.
    """
    def __init__(self: T) -> None:
        self._rule_name = "W391"
        self._message = 'blank line at end of file'

    def test(self: T, ts: CommonTokenStream) -> list:
        tokens = lexer.getAllTokens()
        output: List[tuple] = []
        if len(tokens) == 0:
            return output
        final_token = tokens[-1]
        if ts.LT(1).type == Token.EOL and ts.LT(-1).type == vbaLexer.NEWLINE:
            final_token = ts.LT(-1)
            newline_list = RuleBase.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                output.append((final_token.line + num_nl - 1, 1, "W391"))
        return output
