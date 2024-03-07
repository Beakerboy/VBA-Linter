from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='ArglistWs')


class ArglistWs(ParseTreeListener):
    """
    Inspect the whitespace before an argument list to
    ensure there is no whitespace between the function
    name and the left parenthesis.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterArgumemtList(self: T,  # noqa: N802
                          ctx: vbaParser.ArgumentListContext) -> None:
        """
        Best Practice:
        foo = bar(1, 2, 3)
        Call bar(1, 2, 3)
        """
        token = ctx.start
        if token.LT(-1).type == vbaLexer.LPAREN:
            ws = token.LT(-2)
            if ws.type == vbaLexer.WS:
                self.output.append((ws.line, ws.column, "221"))
        elif token.LT(-2).type == vbaLexer.LPAREN:
            ws = token.LT(-3)
            if ws.type == vbaLexer.WS:
                self.output.append((ws.line, ws.column, "221"))

    def enterProcedureParameters(self: T,  # noqa: N802
                                 ctx: vbaParser.ProcedureParametersContext
                                ) -> None:
        """
        Best Practice:
        foo = bar(1, 2, 3)
        Call bar(1, 2, 3)
        """
        token = ctx.start
        if token.LT(-1).type == vbaLexer.WS:
            ws = token.LT(-1)
            self.output.append((ws.line, ws.column, "221"))

    def enterPropertyParameters(self: T,  # noqa: N802
                                ctx: vbaParser.PropertyParametersContext
                               ) -> None:
        """
        Best Practice:
        foo = bar(1, 2, 3)
        Call bar(1, 2, 3)
        """
        token = ctx.start
        if token.LT(-1).type == vbaLexer.WS:
            ws = token.LT(-1)
            self.output.append((ws.line, ws.column, "221"))
