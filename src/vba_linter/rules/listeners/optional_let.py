from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase

T = TypeVar('T', bound='OptionalLet')


class OptionalLet(ParseTreeListener, RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._severity = 'W'
        self._rule_name = "111"
        self._message = "Optional let"

    def enterLetStmt(self: T,  # noqa: N802
                     ctx: vbaParser.LetStmtContext) -> None:
        token = ctx.start
        if token.type == vbaLexer.LET:
            line = token.line
            column = token.column
            name = self._rule_name
            output = (line, column + 1, name)
            self.output.append(output)
