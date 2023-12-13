from typing import TypeVar
from vba_linter.rules.w200 import W200


T = TypeVar('T', bound='RuleLoader')


class RuleLoader:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules = [W200()]

    def test_all(self: T, tokens: list) -> list:
        output = []
        for rule in self._rules:
            results = rule.test(tokens)
            if results != []:
              output.extend(results)
        return output

    def test_rule(self: T, tokens: list) -> list:
        return []
