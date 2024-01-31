import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.parsing_error import ParsingError


anti_patterns = [
    [
        '''\
Public Function Foo(num)
End Sub
''',  # noqa
        [(2, 4, "999",
          "no viable alternative at input 'End Sub'")]
    ],
    [
        '<?php phpinfo() ?>',
        [(1, 0, "999", "mismatched input '<?php' expecting <EOF>")]
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
