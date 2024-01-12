from antlr4 import CommonTokenStream, ParseTreeListener, ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import Type, TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='MissingVisibility')


class MissingVisibility(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        child = ctx.getChild(0)
        tok = ctx.start
        if isinstance(child, vbaParser.VisibilityContext):
            if tok.text == "Public":
                self.output.append((tok.line, tok.column + 1,
                                    "Wxxx", "optional public"))
        else:
            line = tok.line
            column = tok.column
            msg = "missing visibility"
            self.output.append((line, column + 1, "Wxxx", msg))
