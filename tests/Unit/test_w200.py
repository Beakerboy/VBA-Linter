import pytest
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer
from vba_linter.rules.w200 import W200


eol_ws_data = [
    (
        'Public Function Foo(num) \r\nEnd Function\r\n',
        [(1, "W200")]
    ),
]


@pytest.mark.parametrize("code, expected", eol_ws_data)
def test_eol_ws(code: str, expected: list) -> None:
    input_stream = InputStream(code)
    lexer = vbaLexer(input_stream)
    tokens = lexer.getAllTokens()
    rule = W200()

    assert rule.test(tokens) == expected
