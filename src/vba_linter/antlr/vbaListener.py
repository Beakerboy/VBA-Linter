from antlr4 import ParseTreeListener
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='vbaListener')


class vbaListener(ParseTreeListener):
    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterLetStmt(self: T, ctx:vbaParser.LetStmtContext):
        tok = self.ts.get(ctx.EQ.index - 1)
        if tok.type == vbaLexer.WS:
            if len(tok.text) > 1:
                raise Exception('too many leading spaces')
        else:
            raise Exception('Missing leading space')
