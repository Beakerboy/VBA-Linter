from antlr4 import ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='ParameterUnused')


class ParameterUnused(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._parameters: dict = {}

    def enterParamDcl(self: T,  # noqa: N802
                      ctx: vbaParser.ParamDclContext) -> None:
        arg = ctx.start
        name = arg.start.text
        line = arg.start.line
        column = arg.start.column
        self._parameters[name] = [False, line, column]

    def enterSimpleNameExpression(  # noqa: N802
            self: T,
            ctx: vbaParser.SimpleNameExpressionContext
    ) -> None:
        name = ctx.start.text
        if name in self._parameters:
            self._parameters[name][0] = True

    def exitFunctionStmt(self: T,  # noqa: N802
                         ctx: vbaParser.FunctionStmtContext) -> None:
        self.exit_function_sub_stmt(ctx)

    def exitSubStmt(self: T,  # noqa: N802
                    ctx: vbaParser.SubStmtContext) -> None:
        self.exit_function_sub_stmt(ctx)

    def exit_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        for parameter, data in self._parameters.items():
            if not data[0]:
                msg = "parameter not used"
                self.output.append((data[1], data[2], "700", msg))
        self._parameters = {}
