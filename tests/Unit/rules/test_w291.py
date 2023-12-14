import pytest
from vba_linter.linter import Linter
from vba_linter.rules.w291 import W291


class TestW291(RuleTestBase):

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
