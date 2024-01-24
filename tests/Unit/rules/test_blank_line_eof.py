import pytest
from vba_linter.rules.rule_base import RuleBase
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.blank_line_eof import BlankLineEof


anti_patterns = [
    [RuleTestBase.worst_practice, [(12, 1, "391")]],
    [
        '''\
Public Function Foo(num)
End Function

''',  # noqa
        [(3, 1, "391")]
    ],
    [
        '''\
Public Function Foo(num)
End Function

 
''',  # noqa
        []
    ],
    [
        '''\
Public Function Foo(num)
End Function


''',  # noqa
        [(4, 1, "391")]
    ]
]


rule = BlankLineEof()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "391")
    expected = ":3:13: W391 blank line at end of file"
    assert rule.create_message(data) == expected
