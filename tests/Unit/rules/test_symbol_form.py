import pytest
from vba_linter.rules.rule_base import RuleBase
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.symbol_form import SymbolForm


anti_patterns = [
    [RuleTestBase.worst_practice, [(13, 1, "391")]],
    [
        '''\
Attribute VB_Name = "Foo"
Public Function Foo(num)
if X =< 3 then
foo = 3
end if
End Function

''',  # noqa
        [(3, 6, "183")]
    ]
]


rule = SymbolForm()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (1, 11, "183")
    expected = ":1:11: E183 incorrect symbol format"
    assert rule.create_message(data) == expected
