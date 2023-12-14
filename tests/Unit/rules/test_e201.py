import pytest
from vba_linter.linter import Linter
from vba_linter.rules.e201 import E201


test_data = [
    [
        'Public Function Foo( num)\r\nEnd Function\r\n',
        [(1, 21, "E201")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "E201")]
    ],
]


@pytest.mark.parametrize("code, expected", test_data)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = E201()

    assert rule.test(tokens) == expected


def test_message() -> None:
    rule = E201()
    data = (3, 13, "E201")
    expected = ":3:13: E201 Whitespace after '('"
    assert rule.create_message(data) == expected
