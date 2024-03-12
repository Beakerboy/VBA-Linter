from typing import TypeVar
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='ParserRuleStub')


class ParserRuleStub(ListenerRuleBase):
    def __init__(self: T, name: str) -> None:
        super().__init__()
        self._rule_name = name
