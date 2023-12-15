from typing import Type, TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    rule: RuleBase
    best_practice = [
        [
            ('Public Function Foo(num)\r\n' +
             '    bar = data(1)\r\n' +
             '    baz = (2 + 1)\r\n' +
             'End Function\r\n'),
            []
        ]
    ]

    @classmethod
    def test_test(cls: Type[T], rule: RuleBase,
                  code: str, expected: list) -> None:
        linter = Linter()
        lexer = linter.get_lexer(code)
        tokens = lexer.getAllTokens()
        assert cls.rule.test(tokens) == expected
