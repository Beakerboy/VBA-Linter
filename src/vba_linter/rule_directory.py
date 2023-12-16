from typing import TypeVar
from vba_linter.rules.w291 import W291
from vba_linter.rules.w201 import W201
from vba_linter.rules.w391 import W391
from vba_linter.rules.w500 import W500
from vba_linter.rules.w501 import W501


T = TypeVar('T', bound='RuleDirectory')


class RuleDirectory:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules = []

    def add_rule(self: T, rule: RuleBase) -> None:
        self._rules.append(rule)

    def load_all_rules() -> list:
        return [W291(), W201(), W391(), W500(), W501()]

    def test_all(self: T, tokens: list) -> list:
        output = []
        for rule in self._rules:
            output.extend(rule.test(tokens))
        return output

    def test_rule(self: T, tokens: list) -> list:
        return []
