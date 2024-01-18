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
                    self._parameters[name] = False
            elif isinstance(child, vbaParser.LetStmtContext):
                valueStmts = child.getChildren(
                    lambda x: isinstance(x, vbaParser.ValueStmtContext)
                )
                for valueStmt in valueStmts:
                    if valueStmt.getChildCount() == 1:
                        # literal or parameter
                        ...
                    else:
                        # complex expression
                        ...
        # add new parametrs from let statements
        # add new parameters from variableStmt
        # check off any that are used in procedure calls
        # check off any that are used in a ValueStmt.
