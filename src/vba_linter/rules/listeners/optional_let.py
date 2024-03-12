from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='OptionalLet')


class OptionalLet(ListenerRuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._severity = 'W'
        self._rule_name = "202"
        self._message = "Optional let"

    def enterLetStatement(  # noqa: N802
            self: T,
            ctx: vbaParser.LetStatementContext) -> None:
        token = ctx.start
        if token.type == vbaLexer.LET:
            line = token.line
            column = token.column
            name = self._rule_name
            output = (line, column + 1, name)
            self.output.append(output)

    def enterArgumentList(self: T,  # noqa: N802
                          ctx: vbaParser.ArgumentListContext) -> None:
        # exit()
