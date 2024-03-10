from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.antlr.vbaListener import VbaListener

T = TypeVar('T', bound='MissingLet')


class MissingLet(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._severity = 'W'
        self._rule_name = "201"
        self._message = "Missing let"

    def enterLetStatement(self: T,  # noqa: N802
                          ctx: vbaParser.LetStatementContext) -> None:
        token = ctx.start
        if token.type != vbaLexer.LET:
            line = token.line
            column = token.column
            name = self._rule_name
            output = (line, column + 1, name)
            self.output.append(output)
