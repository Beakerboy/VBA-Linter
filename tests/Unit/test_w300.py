import pytest
from vba_linter.linter import Linter
from vba_linter.rules.w200 import W200


extra_eol = [
    [
        'Public Function Foo(num)\r\nEnd Function\r\n\r\n',
        [(3, 0, "W300")]
    ],
    [
        'Public Function Foo(num)\r\nEnd Function\r\n\r\n\r\n',
        [(3, 0, "W300"), (4, 0, "W300")]
    ]
]


@pytest.mark.parametrize("code, expected", eol_ws_data)
def test_extra_endlines(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = W300()

    assert rule.test(tokens) == expected
