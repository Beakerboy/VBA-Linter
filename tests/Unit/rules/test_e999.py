import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    ['''\
Function Foo()
End Sub
''',  # noqa
     [(1, 0, "E999")]],
    ['<?php phpinfo(); ?>', [(1, 0, "E999")]]
]


@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(code: str, expected: tuple) -> None:
    linter = Linter()
    assert linter.lint(code) == expected
