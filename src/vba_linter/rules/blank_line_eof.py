from antlr4 import CommonTokenStream, Token
from antlr4_vba import vbaLexer
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
        output: List[tuple] = []
        if (ts.index > 0):
            output = [(1, 1, 1)]
            if (ts.LA(1) == Token.EOF):
                output = [(2, 2, 2)]
                if (ts.LA(-1) == vbaLexer.NEWLINE):
                    final_token = ts.LT(-1)
                    output = [(1, 2, 3)]
                    newline_list = RuleBase.split_nl(final_token.text)
                    num_nl = len(newline_list)
                    if num_nl > 1:
                        output = [(final_token.line + num_nl - 1, 1, "W391")]
        return output
