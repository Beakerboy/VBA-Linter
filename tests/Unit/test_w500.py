import pytest
from vba_linter.linter import Linter
from vba_linter.rules.w200 import W200


line_ending_data = [
    ('\r\n', []),
    ('\r\n\r\n', []),
    ('\n\r\nFunction Foo()\r\n\r\nEnd Function\r\n', [(1, 1, "W500")]),
    ('\r\n\nFunction Foo()\r\n\r\nEnd Function\r\n', [(2, 1, "W500")]),
    ('\r\n\r\nFoo\n', [(3, 3, "W500")]),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        [(2, 12, "W500")]
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        [(1, 24, "W500"), (2, 12, "W500")]
    ),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: list) -> None:
    linter = Linter()
    tokens = linter.get_lexer(code).getAllTokens()
    rule = W500()

    assert rule.test(tokens) == expected
