from antlr4 import ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='MissingVisibility')


class MissingVisibility(ParseTreeListener, RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._rule_name = "510"
        self._message = "Missing visibility"

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        child = ctx.getChild(0)
        tok = ctx.start
        if not isinstance(child, vbaParser.VisibilityContext):
            line = tok.line
            column = tok.column
            msg = "missing visibility"
            self.output.append((line, column + 1, "Wxxx", msg))
