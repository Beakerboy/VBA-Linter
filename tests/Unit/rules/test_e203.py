import pytest
from vba_linter.linter import Linter
from vba_linter.rules.e203 import E203


test_data = [
    [
        'Public Function Foo(num , bar)\r\nEnd Function\r\n',
        [(1, 24, "E203")]
    ],
    [
        'Foo = Bar num , baz\r\n',
        [(1, 14, "E203")]
    ],
    [
        'Foo = Bar a, b , c\r\n',
        [(1, 13, "E203")]
    ],
]


@pytest.mark.parametrize("code, expected", test_data)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = E203()

    assert rule.test(tokens) == expected
