from testing import TypeVar
from tests.rules.rules_test_base import RulesTestBase
from vba_linter.rules.w291 import W291


T = TypeVar('T', bound='TestW291')


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
'''),  # noqa
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


best_practice = [
    ['''\
Public Function Foo(num)

End Function
''',  # noqa
       []]
]


@pytest.mark.parametrize("code, expected", anti_patterns + best_practice)
class TestW291(RuleTestBase):
    def __init__(self: T) -> None:
        self.rule = W291()
