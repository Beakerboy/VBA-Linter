import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.multiple_spaces_comma import MultipleSpacesComma


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(1, 80, 'E241')]
    ]
]


rule = MultipleSpacesComma()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 80, "W501", 86)
    expected = ":3:80: W501 line too long (86 > 79 characters)"
    assert rule.create_message(data) == expected
