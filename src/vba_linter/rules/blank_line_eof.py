from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='BlankLineEof')


class BlankLineEof(RuleBase):
    """
    Returns an error if the final line is solely a newline character.
    """
    def __init__(self: T) -> None:
        self._severity = 'W'
        self._rule_name = "391"
        self._message = 'blank line at end of file'

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        if (ts.index > 0 and ts.LA(1) == vbaLexer.NEWLINE and
                ts.LA(2) == Token.EOF):
            final_token = ts.LT(1)
            assert final_token is not None
            newline_list = RuleBase.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                output = [(final_token.line + num_nl - 1, 1, "391")]
                final_token.text = "\r\n"
        return output
