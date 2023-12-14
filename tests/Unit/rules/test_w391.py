import pytest
from typing import TypeVar
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.w391 import W391


T = TypeVar('T', bound='TestW391')

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


best_practice = [
    ['''\
Public Function Foo(num)
End Function
''',  # noqa
     []
]]


@pytest.mark.parametrize("code, expected", anti_patterns + best_practice)
class TestW391(RuleTestBase):
    def __init__(self: T) -> None:
        self.rule = W391()
