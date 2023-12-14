import pytest
from vba_linter.linter import Linter
from vba_linter.rules.w291 import W291


test_data = [
    [
        'Public Function Foo(num) \r\nEnd Function\r\n',
        [(1, 25, "W291")]
    ],
    [
        'Public Function Foo(num)\r\n\r\nEnd Function \r\n',
        [(3, 13, "W291")]
    ],
    [
        'Public Function Foo(num)\r\n\nEnd Function \r\n',
        [(3, 13, "W291")]
    ],
]


@pytest.mark.parametrize("code, expected", test_data)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = W291()

    assert rule.test(tokens) == expected


def test_message() -> None:
    rule = W200()
    data = (3, 13, "W291")
    expected = ":3:13: W291 trailing whitespace"
    assert rule.create_message(data) == expected
