from typing import Type, TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    best_practice = [
        ['', []],
        ['\r\n', []],
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
        assert rule.test(tokens) == expected

    @classmethod
    def tokenize(cls: Type[T], rule: RuleBase, code: str) -> None:
        linter = Linter()
        lexer = linter.get_lexer(code)
        return rule.test(lexer.getAllTokens())
