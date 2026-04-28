import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.arglist_ws import ArglistWs


msg = "Excess whitespace before '('"


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(2, 51, '121', msg)]
    ],
    [
        '''\
Attribute VB_Name = "Foo"
Public Sub Foo (num)
    Call Foo (3)
    Foo (1 + 2)
    bar = Foo (1 + 2)
End Sub

Public Property Let Bar (bar)
End Property
''',  # noqa
        [(2, 15, "121", msg),
         (3, 13, "121", msg),
         (5, 14, "121", msg),
         (8, 24, "121", msg)]
    ]
]


rule = ArglistWs()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected", anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
