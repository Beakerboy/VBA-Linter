import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.stream.ambiguous_identifier import AmbiguousIdentifier


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(6, 1, '741')]
    ],
    [
        '''\
Attribute VB_Name = "Foo"
Public Function Foo(num)
    Dim l as Integer
End Function
''',  # noqa
        [(3, 9, "741")]
    ]
]


rule = AmbiguousIdentifier()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (4, 1, "741")
    expected = ":4:1: E741 ambiguous variable name"
    assert rule.create_message(data) == expected
