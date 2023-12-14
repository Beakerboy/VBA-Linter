import pytest
from vba_linter.linter import Linter
from vba_linter.rules.w291 import W291


anti_patterns = [
    [
        ('''\
Public Function Foo(num) 
End Function
'''  # noqa),
        [(1, 25, "W291")]
    ],
    [
        ('Public Function Foo(num)\r\n' +
         '\r\n' +
         'End Function \r\n'),
        [(3, 13, "W291")]
    ],
    [
        ('Public Function Foo(num)\r\n' +
         '\n' +
         'End Function \r\n'),
        [(3, 13, "W291")]
    ],
]


best_practice = [
    [('Public Function Foo(num)\r\n' +
      'End Function\r\n'),
      []]
]


@pytest.mark.parametrize("code, expected", anti_patterns + best_practice)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = W291()

    assert rule.test(tokens) == expected


def test_message() -> None:
    rule = W291()
    data = (3, 13, "W291")
    expected = ":3:13: W291 trailing whitespace"
    assert rule.create_message(data) == expected
