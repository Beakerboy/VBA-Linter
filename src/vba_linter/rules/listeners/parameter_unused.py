from antlr4 import CommonTokenStream, ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='ParameterUnused')


class ParameterUnused(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._parameter_list: dict = {}

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        # go to the arglist context to get the parameters
        # add new parametrs from let statements
        # add new parameters from variableStmt
        # check off any that are used in procedure calls
        # check off any that are used in a ValueStmt.
              
