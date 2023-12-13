from typing import TypeVar
from vba_linter.rules.w200 import W200
from vba_linter.rules.w501 import W501



T = TypeVar('T', bound='RuleLoader')


class RuleLoader:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules = [W200(), W501()]

    def test_all(self: T, tokens: list) -> list:
        output = []
        for rule in self._rules:
            output.extend(rule.test(tokens))
        return output

    def test_rule(self: T, tokens: list) -> list:
        return []
