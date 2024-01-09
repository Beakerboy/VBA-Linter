from vba_linter.antlr.thrown_exception import ThrownException
from antlr4_vba.vbaParser import vbaParser
from vba_linter.antlr.throwing_error_listener import ThrowingErrorListener
from antlr4 import CommonTokenStream
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='ParsingError')


class ParsingError(RuleBase):
    def __init__() -> None:
        self.program = None
        self.parser = None

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        parser = vbaParser(ts)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener())
        self.parser = parser
        try:
            self.program = parser.startRule()
        except ThrownException as ex:
            return [(ex.line, ex.column, "E999", ex.msg)]
        return output

    def create_message(self: T, data: tuple) -> str:
        return (":%s:%s: %s %s") % data
