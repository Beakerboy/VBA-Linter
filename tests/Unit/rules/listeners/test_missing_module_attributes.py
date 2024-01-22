import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.missing_module_attributes import MissingModuleAttributes


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(1, 1, '601')]
    ]
]


rule = MissingModuleAttributes()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected", anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
