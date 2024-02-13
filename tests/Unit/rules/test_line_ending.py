import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.line_ending import LineEnding


anti_patterns = [
    (
        RuleTestBase.worst_practice,
        [
            (2, 92, "500"),
            (3, 0, "500"),
            (5, 11, "500"),
            (9, 12, "500")
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
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "500")
    expected = ":3:13: E500 incorrect line ending"
    assert rule.create_message(data) == expected
