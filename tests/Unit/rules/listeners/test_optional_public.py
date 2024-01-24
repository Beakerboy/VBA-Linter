import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.optional_public import (
    OptionalPublic)


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(1, 1, '505')]
    ]
]


rule = OptionalPublic()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected", anti_patterns
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
