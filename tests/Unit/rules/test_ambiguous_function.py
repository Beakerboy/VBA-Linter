import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.ambiguous_identifier import AmbiguousIdentifier


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(8, 17, 'E743')]
    ]
]


rule = AmbiguousIdentifier()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (4, 1, "E743")
    expected = ":4:1: E741 ambiguous function name"
    assert rule.create_message(data) == expected
