import pytest
from typing import TypeVar
from Unit.rules.rule_test_base import RuleTestBase
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


T = TypeVar('T', bound='TestW291')


@pytest.mark.parametrize('rule', W291())
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
class TestW291(RuleTestBase):
    def test_message(self: T) -> None:
        data = (3, 13, "W291")
        rule = W291()
        expected = ":3:13: W291 trailing whitespace"
        assert rule.create_message(data) == expected
