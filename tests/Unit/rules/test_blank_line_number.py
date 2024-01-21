import pytest
from vba_linter.rules.rule_base import RuleBase
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.blank_line_number import BlankLineNumber


anti_patterns = [
    [RuleTestBase.worst_practice, [(4, 0, "303")]],
]


rule = BlankLineNumber()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (4, 0, "303")
    expected = ":4:0: W303 too many blank lines (3)"
    assert rule.create_message(data) == expected
