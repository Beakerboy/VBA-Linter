import pytest
from vba_linter.rule_directory import RuleDirectory
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    [
        'Public Function Foo(num )\r\nEnd Function\r\n',
        [(1, 24, "E202")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "E202")]
    ],
]


rd = RuleDirectory()
rd.load_all_rules()
rule = rd.get_rule("E202")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase(rule, code) == expected
