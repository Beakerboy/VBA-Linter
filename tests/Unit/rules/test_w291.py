import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w291 import W291


anti_patterns = [
    [
        '''\
Public Function Foo(num) 
End Function
''',  # noqa
        [(1, 25, "W291")]
    ],
    [
        '''\
Public Function Foo(num)

End Function 
''',  # noqa
        [(3, 13, "W291")]
    ],
    [
        '''\
Public Function Foo(num)
 
End Function
''',  # noqa
        [(2, 1, "W291")]
    ],
]


message_data = [
    [(3, 13, "W291"), ":3:13: W291 trailing whitespace"],
    [(2, 1, "W291"), ":2:1: W202 blank line contains whitespace"]
]


rule = W291()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "data, expected", message_data
)
def test_message(rule: RuleBase, data: tuple, expected: str) -> None:
    assert rule.create_message(data) == expected
