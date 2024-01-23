import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.ambiguous_function import AmbiguousFunction


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(10, 10, '743')]
    ]
]


rule = AmbiguousFunction()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (4, 1, "743")
    expected = ":4:1: E743 ambiguous function name"
    assert rule.create_message(data) == expected
