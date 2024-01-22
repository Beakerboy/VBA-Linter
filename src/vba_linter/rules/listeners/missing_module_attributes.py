from antlr4 import ParseTreeListener, TerminalNode
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='MissingModuleAttributes')


class MissingModuleAttributes(ParseTreeListener, RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "601"
        self._message = "missing module attributes"
        self.output: list = []
        self._found = False

    def enterModuleAttributes(  # noqa: N802
            self: T,
            ctx: vbaParser.ModuleAttributesContext
    ) -> None:
        self._found = True

    def visitTerminal(self: T, node: TerminalNode) -> None:  # noqa: 
        if not self._found:
            name = self._rule_name
            msg = self._message
            self.output = [(1, 1, name)]
