from antlr.vbaLexer import vbaLexer
from antlr4 import InputStream
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='E101')


class E101(RuleBase):
    """
    report if a non-blank line has a mix of chars
    in the leading whitespace
    """
    def __init__(self: T) -> None:
        self._rule_name = 'E101'
        self._message = "indentation contains mixed spaces and tabs"

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        try:
            input_stream = InputStream(code)
        except:
            output = [(1, 1, "E999")]
        return output
