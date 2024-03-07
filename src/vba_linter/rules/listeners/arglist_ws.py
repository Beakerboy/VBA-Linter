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

    def enterArgList(self: T,  # noqa: N802
                          ctx: vbaParser.ArgListContext) -> None:
        """
        foo = bar(1, 2, 3)
        Call bar(1, 2, 3)
        """
        token = ctx.start
        if token.LT(-1).symbol == vbaLexer.LPAREN:
            ws = token.LT(-2)
            if ws.symbol == vbaLexer.WS:
                self.output.append((ws.line, ws.column, "221"))
        elif token.LT(-2).symbol == vbaLexer.LPAREN:
            ws = token.LT(-3)
            if ws.symbol == vbaLexer.WS:
                self.output.append((ws.line, ws.column, "221"))
