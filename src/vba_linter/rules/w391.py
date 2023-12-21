from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W391')


class W391(RuleBase):
    """
    Returns an error if the final line is solely a newline character.
    """
    def __init__(self: T) -> None:
        self._rule_name = "W391"
        self._message = 'blank line at end of file'

    def test(self: T, lexer: vbaLexer) -> list:
        tokens = lexer.getAllTokens()
        output: list[tuple] = []
        if len(tokens) == 0:
            return output
        final_token = tokens[-1]
        if final_token.type == vbaLexer.NEWLINE:
            newline_list = RuleBase.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                output.append((final_token.line + num_nl - 1, 1, "W391"))
        return output
