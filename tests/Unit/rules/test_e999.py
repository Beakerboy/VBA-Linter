import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.parsing_error import ParsingError


txt = ("extraneous input '<?php' expecting " +
       "{'ATTRIBUTE', 'VERSION', NEWLINE, REMCOMMENT, COMMENT, WS}")
anti_patterns = [
    [
        '''\
Attribute VB_Name = "Foo"
Public Function Foo(num)
End Sub
''',  # noqa
        [(3, 4, "999",
          "mismatched input 'Sub' expecting 'FUNCTION'")]
    ],
    [
        '<?php phpinfo() ?>',
        [(1, 0, "999", txt)]
    ],
]


@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(code: str, expected: tuple) -> None:
    rule = ParsingError()
    file_name = RuleTestBase.save_code(code)
    ts = RuleTestBase.create_tokens(file_name)
    assert rule.test(ts) == expected
    RuleTestBase.delete_code(file_name)


def test_message() -> None:
    rule = ParsingError()
    data = (1, 0, "999", "mismatched input '<?php' expecting <EOF>")
    expected = ":1:0: F999 mismatched input '<?php' expecting <EOF>"
    assert rule.create_message(data) == expected
