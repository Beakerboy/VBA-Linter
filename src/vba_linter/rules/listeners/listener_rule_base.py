from antlr4 import ParseTreeListener
from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='ListenerRuleBase')


class ListenerRuleBase(ParseTreeListener, RuleBase):
    """
    A common interface for ListenerRules.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
