import pytest
from typing import TypeVar
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.w391 import W391


anti_patterns = [
    [
        '''\
Public Function Foo(num)
End Function

''',  # noqa
        [(3, 0, "W300")]
    ],
    [
        '''\
Public Function Foo(num)
End Function


''',  # noqa
        [(3, 0, "W300"), (4, 0, "W300")]
    ]
]


RuleTestBase.rule = W391()


@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(code, expected) -> None:
    RuleTestBase(code, expected)
    

def test_message() -> None:
    data = (3, 13, "W391")
    rule = W391()
    expected = ":3:13: W391 blank line at end of file"
    assert rule.create_message(data) == expected
