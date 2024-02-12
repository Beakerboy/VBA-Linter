from antlr4 import CommonTokenStream, ParserRuleContext
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='FunctionNaming')


class FunctionNaming(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._message = "name not Pascal"

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        tokens = VbaListener.get_tokens(ctx)
        token = tokens[2]
        if tokens[2].type == vbaLexer.IDENTIFIER:
            token = tokens[2]
        else:
            assert tokens[4].type == vbaLexer.IDENTIFIER
            token = tokens[4]
        if not VbaListener.is_pascal_case(token.text):
            line = token.line
            column = token.column
            self.output.append((line, column + 2, "Wxxx"))
