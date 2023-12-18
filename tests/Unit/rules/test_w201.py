import pytest
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w201 import W201
from Unit.rules.rule_test_base import RuleTestBase


anti_patterns = [
    ['''\
Public Function Foo(num)
End Function''',  # noqa
     [(2, 12, 'W201')]]
]


rule = W201()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected
