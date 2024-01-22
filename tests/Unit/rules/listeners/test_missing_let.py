import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.missing_let import MissingLet


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(5, 1, '110'), (6, 5, '110')]
    ]
]


rule = MissingLet()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected", anti_patterns
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
