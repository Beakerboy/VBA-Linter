from antlr4 import CommonTokenStream, ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='vbaListener')


class vbaListener(ParseTreeListener):
    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterLetStmt(self: T, ctx:vbaParser.LetStmtContext):
        for child in ctx.getChildren():
            if child.symbol.type == vbaLexer.EQ:
                target = child.symbol
            break
        leading_index = target.tokenIndex - 1
        # trailing_index = target.getTokenIndex() - 1
        tok = self.ts.get(leading_index)
        if tok.type == vbaLexer.WS:
            if len(tok.text) > 1:
                raise Exception('too many leading spaces')
        else:
            raise Exception('Missing leading space')
