from antlr4 import CommonTokenStream, ParseTreeListener
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='vbaListener')


class vbaListener(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterLetStmt(self: T, ctx:vbaParser.LetStmtContext):
        for child in ctx.getChildren():
            terminal_num = 0
            if isinstance(child, TerminalNodeImpl):
                tok = child.getSymbol()
                terminal_num += 1
                if terminal_num == 1 and tok.type != vbaLexer.LET:
                    self.output.append((tok.line, tok.column + 2, "Wxxx", "missing let"))
                if tok.type == vbaLexer.LET:
                    self.output.append((tok.line, tok.column + 2, "Wxxx", "optional let"))
                if tok.type == vbaLexer.EQ:
                    target = tok
                    leading_index = target.tokenIndex - 1
                    trailing_index = target.tokenIndex + 1
                    tok = self.ts.get(leading_index)
                    if tok.type == vbaLexer.WS:
                        if len(tok.text) > 1:
                            self.output.append((tok.line, tok.column + 2, "W221"))
                    else:
                        self.output.append((target.line, target.column + 1, "R225"))
                    tok = self.ts.get(leading_index)
                    if tok.type == vbaLexer.WS:
                        if len(tok.text) > 1:
                            self.output.append((tok.line, tok.column + 2, "W221"))
                    else:
                        self.output.append((target.line, target.column + 1, "R225"))
                    
