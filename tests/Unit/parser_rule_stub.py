from antlr4 import ParseTreeListener
from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase

T = TypeVar('T', bound='ParserRuleStub')


class ParserRuleStub(ParseTreeListener, RuleBase):
    def __init__(self: T, name: str) -> None:
        super().__init__()
        self._rule_name = name
