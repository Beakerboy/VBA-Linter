import pytest
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    [
        'Public Function Foo(num , bar)\r\nEnd Function\r\n',
        [(1, 24, "E203")]
    ],
    [
        'Foo = Bar num , baz\r\n',
        [(1, 14, "E203")]
    ],
    [
        'Foo = Bar a, b , c\r\n',
        [(1, 15, "E203")]
    ],
    [
        'Public Function Foo(num ; bar)\r\nEnd Function\r\n',
        []
    ]
]


rd = RuleDirectory()
rd.load_all_rules()
rule = rd.get_rule("E203")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    assert rule.test(lexer) == expected
