from antlr4 import ParseTreeListener
from typing import TypeVar


T = TypeVar('T', bound='vbaListener')


class vbaListener(ParseTreeListener):
    def enterLetStmt(self: T, ctx:vbaParser.LetStmtContext):
        pass
