from antlr.thrown_exception import ThrownException
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from antlr.throwing_error_listener import ThrowingErrorListener
from antlr4 import CommonTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='E999')


class E999(RuleBase):

    def test(self: T, lexer: vbaLexer) -> list:
        output: list[tuple] = []
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())

        stream = CommonTokenStream(lexer)
        parser = vbaParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener())
        try:
            parser.startRule()
        except ThrownException as ex:
            return [(ex.line, ex.column, "E999", ex.msg)]
        return output

    def create_message(self: T, data: tuple) -> str:
        return (":%s:%s: %s %s") % data
