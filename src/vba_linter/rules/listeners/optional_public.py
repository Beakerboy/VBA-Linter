from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='OptionalPublic')


class OptionalPublic(ListenerRuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._message = "Optional public"
        self._rule_name = "505"

    def enterProcedureScope(self: T,  # noqa: N802
                            ctx: vbaParser.ProcedureScopeContext) -> None:
        tok = ctx.start
        if tok.text == "Public":
            line = tok.line
            column = tok.column
            self.output.append((line, column + 1, self._rule_name))
