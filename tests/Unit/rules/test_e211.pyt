import pytest
from vba_linter.linter import Linter
from vba_linter.rules.e211 import E211


anti_patterns = [
    [
        '''\
Public Function Foo (num)
End Function
''',  # noqa
        [(1, 20, "E211")]
    ],
    [
        '''\
Public Function Foo(data)
    bar = data (1)
End Function
''',  # noqa
        [(2, 15, "E211")]
    ],
]


best_practice = [
    ['''\
Public Function Foo(data)
    bar = data(1)
    baz = (2 + 1)
End Function
''',  # noqa
     []]
]


@pytest.mark.parametrize("code, expected", anti_patterns + best_practice)
def test_test(code: str, expected: list) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = E211()

    assert rule.test(tokens) == expected


def test_message() -> None:
    rule = W291()
    data = (3, 13, "W291")
    expected = ":3:13: W291 trailing whitespace"
    assert rule.create_message(data) == expected
