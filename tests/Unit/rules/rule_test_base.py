from typing import TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    def __init__(self: T) -> None:
        self.best_practice = [
            ['''\
Public Function Foo(num)
End Function
''',  # noqa
             []
            ]
        ]
        self.rule: RuleBase

    def test_test(self: T, code: str, expected: list) -> None:
        linter = Linter()
        lexer = linter.get_lexer(code)
        tokens = lexer.getAllTokens()
        assert self.rule.test(tokens) == expected

    def test_message(self: T) -> None:
        data = (3, 13, "W291")
        expected = ":3:13: W291 trailing whitespace"
        assert self.rule.create_message(data) == expected
