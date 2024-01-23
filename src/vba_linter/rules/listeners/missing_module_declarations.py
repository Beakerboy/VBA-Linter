from antlr4 import TerminalNode
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='MissingModuleAttributes')


class MissingModuleDeclarations(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "602"
        self._message = "Missing module declarations"
        self.output: list = []
        self._found = False

    def enterStartRule(  # noqa: N802
            self: T,
            ctx: vbaParser.StartRuleContext) -> None:
        self.output = []
        self._found = False

    def enterModuleDeclarations(  # noqa: N802
            self: T,
            ctx: vbaParser.ModuleDeclarationsContext
    ) -> None:
        self._found = True

    def enterModuleBody(  # noqa: N802
            self: T,
            ctx: vbaParser.ModuleBodyContext) -> None:
        if not self._found:
            line = ctx.start.line
            column = ctx.start.column
            name = self._rule_name
            self.output.append((line, column + 1, name))
