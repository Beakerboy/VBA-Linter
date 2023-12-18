import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rule_directory import RuleDirectory
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    [
        'Public Function Foo( num)\r\nEnd Function\r\n',
        [(1, 21, "E201")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "E201")]
    ],
]


rd = RuleDirectory()
rd.load_all_rules()
rule = rd.get_rule("E201")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "E201")
    expected = ":3:13: E201 Whitespace after '('"
    assert rule.create_message(data) == expected
