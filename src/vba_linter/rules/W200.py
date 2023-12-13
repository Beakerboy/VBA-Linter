from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar

T = TypeVar('T', bound='W200')

class W200(RuleBase):
    def __init__(self: T) -> None
        self.rule_name = "W200"

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + "Unexpected whitespace at the end of the line"
