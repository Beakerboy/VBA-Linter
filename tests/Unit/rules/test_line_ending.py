import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.line_ending import LineEnding


anti_patterns = [
    ('\n\r\nFunction Foo()\r\n\r\nEnd Function\r\n', [(1, 0, "W500")]),
    ('\r\n\nFunction Foo()\r\n\r\nEnd Function\r\n', [(2, 0, "W500")]),
    ('\r\n\r\nFoo\n', [(3, 3, "W500")]),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        [(2, 12, "W500")]
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        [(1, 24, "W500"), (2, 12, "W500")]
    ),
    (
        RuleTestBase.best_practice,
        [
            (1, 91,"W500"),
            (2, 0,"W500"),
            (3, 13,"W500"),
            (4, 12,"W500"),
        ]
    )
]


rule = LineEnding()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "W500")
    expected = ":3:13: W500 incorrect line ending"
    assert rule.create_message(data) == expected
