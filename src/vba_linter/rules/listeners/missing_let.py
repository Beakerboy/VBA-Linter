from antlr4 import ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='MissingVisibility')


class MissingLet(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterLetStmt(self: T,  # noqa: N802
                     ctx: vbaParser.LetStmtContext) -> None:
        tokens = VbaListener.get_tokens(ctx)
        terminal_num = 0
        for tok in tokens:
            terminal_num += 1
            if terminal_num == 1 and tok.type != vbaLexer.LET:
                output = (tok.line, tok.column + 1, "Wxxx", "missing let")
                self.output.append(output)
