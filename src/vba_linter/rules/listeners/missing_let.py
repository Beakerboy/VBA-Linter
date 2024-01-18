from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='MissingLet')


class MissingLet(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterLetStmt(self: T,  # noqa: N802
                     ctx: vbaParser.LetStmtContext) -> None:
        token = ctx.start
        if token.type != vbaLexer.LET:
            line = token.line
            column = token.column
            output = (line, column + 1, "110", "missing let")
            self.output.append(output)
