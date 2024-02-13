from antlr4 import ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='MissingVisibility')


class MissingVisibility(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._rule_name = "510"
        self._severity = 'W'
        self._message = "Missing visibility"

    def enterFunctionDeclaration(  # noqa: N802
            self: T,
            ctx: vbaParser.FunctionDeclarationContext
    ) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubroutineDeclaration(  # noqa: N802
            self: T,
            ctx: vbaParser.SubroutineDeclarationContext
    ) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        child = ctx.getChild(0)
        tok = ctx.start
        if not isinstance(child, vbaParser.VisibilityContext):
            line = tok.line
            column = tok.column
            name = self._rule_name
            self.output.append((line, column + 1, name))
