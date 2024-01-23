from antlr4 import TerminalNode
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='MissingModuleAttributes')


class MissingModuleAttributes(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "601"
        self._message = "Missing module attributes"
        self.output: list = []
        self._found = False

    def enterStartRule(  # noqa: N802
            self: T,
            ctx: vbaParser.StartRuleContext) -> None:
        self.output = []
        self._found = False

    def enterModuleAttributes(  # noqa: N802
            self: T,
            ctx: vbaParser.ModuleAttributesContext
    ) -> None:
        self._found = True

    def visitTerminal(self: T, node: TerminalNode) -> None:  # noqa: 
        if not self._found:
            line = node.line
            column = node.column
            self.output.append((line, column + 1, self._rule_name))
