from antlr4 import CommonTokenStream, ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='ParameterUnused')


class ParameterUnused(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._parameters: dict = {}

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def exitFunctionStmt(self: T,  # noqa: N802
                         ctx: vbaParser.FunctionStmtContext) -> None:
        self.exit_function_sub_stmt(ctx)

    def exitSubStmt(self: T,  # noqa: N802
                    ctx: vbaParser.SubStmtContext) -> None:
        self.exit_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        children = ctx.getChildren()
        # go to the arglist context to get the parameters
        for child in children:
            if isinstance(child, vbaParser.ArgListContext):
                args = child.getChildren(
                    lambda x: isinstance(x, vbaParser.ArgContext)
                )
                for arg in args:
                    name = arg.start.text
                    line = arg.start.line
                    column = arg.start.column
                    self._parameters[name] = [False, line, column]
            elif isinstance(child, vbaParser.LetStmtContext):
                value_stmts = child.getChildren(
                    lambda x: isinstance(x, vbaParser.ValueStmtContext)
                )
                for value_stmt in value_stmts:
                    self.manage_valuestmt(value_stmt)
        # add new parametrs from let statements
        # add new parameters from variableStmt
        # check off any that are used in procedure calls
        # check off any that are used in a ValueStmt.

    def manage_valuestmt(self: T, ctx: ParserRuleContext) -> None:
        if ctx.getChildCount() == 1:
            # literal or parameter
            call = ctx.getChild().getChild()
            if call.getChildCount() == 1:
                name = call.start.text
                if name in self._parameters:
                    self._parameters[name][0] = True
        else:
            # complex expression
            ...

    def exit_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        for parameter, data in self._parameters.items():
            if not data[0]:
                msg = "parameter not used"
                self.output.append(data[1], data[2], "700", msg)
        self._parameters = {}
