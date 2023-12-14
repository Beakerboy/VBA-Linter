from typing import TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    rule: RuleBase
    best_practice = [
        ['''\
Public Function Foo(num)
End Function
''',  # noqa
         []]
    ]

    def test_test(self: T, rule: RuleBase,
                  code: str, expected: list) -> None:
        linter = Linter()
        lexer = linter.get_lexer(code)
        tokens = lexer.getAllTokens()
        assert RuleTestBase.rule.test(tokens) == expected

    def test_message(self: T, rule: RuleBase) -> None:
        data = (3, 13, "W291")
        expected = ":3:13: W291 trailing whitespace"
        assert rule.create_message(data) == expected
