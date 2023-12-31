import pytest
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w201 import W201
from Unit.rules.rule_test_base import RuleTestBase


anti_patterns = [
    ['''\
Public Function Foo(num)
End Function''',  # noqa
     [(2, 13, 'W201')]]
]


message_data = [
    [(2, 1, "W201"), ":2:1: W201 no newline at end of file"],
 ]


rule = W201()


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
