from antlr4 import ParseTreeListener, TerminalNode
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='MissingModuleAttributes')


class MissingModuleAttributes(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._found = False

    def enterModuleAttributes(  # noqa: N802
            self: T,
            ctx: vbaParser.ModuleAttributesContext
    ) -> None:
        self._found = True

    def visitTerminal(self: T, node: TerminalNode) -> None:  # noqa: 
        if not self._found:
            self.output = [(1, 1, "601", "missing module attributes")]
