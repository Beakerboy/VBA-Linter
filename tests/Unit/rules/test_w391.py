import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w391 import W391


anti_patterns = [
    [
        '''\
Public Function Foo(num)
End Function

''',  # noqa
        [(3, 0, "W300")]
    ],
    [
        '''\
Public Function Foo(num)
End Function


''',  # noqa
        [(3, 0, "W300"), (4, 0, "W300")]
    ]
]


rule = W391()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    RuleTestBase.test_test(rule, code, expected)


def test_message(rule: RuleBase) -> None:
    data = (3, 13, "W391")
    expected = ":3:13: W391 blank line at end of file"
    assert rule.create_message(data) == expected
