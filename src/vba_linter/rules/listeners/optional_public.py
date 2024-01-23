from antlr4 import ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='OptionalPublic')


class OptionalPublic(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        tok = ctx.start
        if tok.text == "Public":
            line = tok.line
            column = tok.column
            msg = "optional public"
            self.output.append((line, column + 1, "505", msg))
