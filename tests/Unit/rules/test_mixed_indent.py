import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.mixed_indent import MixedIndent


anti_patterns = [
    [
        '''\
Public Function Foo(num)
    If True Then
    \tBar = 2
    End If
End Function
''',  # noqa
        [(3, 1, "101")]
    ],
]


message_data = [
    [(3, 1, "101"), ":3:1: E101 indentation contains mixed spaces and tabs"],
 ]


rule = MixedIndent()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "data, expected", message_data
)
def test_message(rule: RuleBase, data: tuple, expected: str) -> None:
    assert rule.create_message(data) == expected
