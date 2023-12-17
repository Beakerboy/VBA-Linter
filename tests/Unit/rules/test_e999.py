import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.linter import Linter


anti_patterns = [
    [
        '''\
Public Function Foo(num)
End Sub
''',  # noqa
        [('x', 'x' "E999")]
    ],
    [
        '<?php phpinfo() ?>',
        [('x', 'x' "E999")]
    ],
]


@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(code: str, expected: tuple) -> None:
    linter = Linter()
    assert linter.lint(code) == expected
