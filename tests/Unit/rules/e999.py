import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.e999 import E999


anti_patterns = [
    ('''\
Function Foo()
End Sub
''',  # noqa
     [(1, 0, "E999")]),
]


rule = E999()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    RuleTestBase.test_test(rule, code, expected)


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "E999")
    expected = ":3:13: E999 Foo"
    assert rule.create_message(data) == expected
