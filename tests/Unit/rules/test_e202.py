import pytest
from vba_linter.linter import Linter
from vba_linter.rules.e202 import E202


test_data = [
    [
        'Public Function Foo(num )\r\nEnd Function\r\n',
        [(1, 24, "W202")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(3, 11, "W200")]
    ],
]


@pytest.mark.parametrize("code, expected", test_data)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = W202()

    assert rule.test(tokens) == expected
