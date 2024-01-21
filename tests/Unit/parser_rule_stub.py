from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase

T = TypeVar('T', bound='ParserRuleStub')


class ParserRuleStub(ParseTreeListener, RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
