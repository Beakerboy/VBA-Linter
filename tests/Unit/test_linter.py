import pytest
from vba_linter.linter import Linter


line_ending_data = [
    ('\r\n', []),
    ('\r\n\r\n', []),
    ('\n\r\n', [(1, "W400")]),
    ('\r\n\n', [(2, "W400")]),
    ('\r\n\r\nFoo\n', [(3, "W400")]),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        [(2, "W400")]
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        [(1, "W400"), (2, "W400")]
    ),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: list) -> None:
    linter = Linter()
    assert linter.lint(code) == expected


eol_ws_data = [
    (
        'Public Function Foo(num) \r\nEnd Function\r\n',
        [(1, "W200")]
    ),
]


@pytest.mark.parametrize("code, expected", eol_ws_data)
def test_eol_ws(code: str, expected: list) -> None:
    linter = Linter()
    assert linter.lint(code) == expected


def test_sort() -> None:
    """
    Test that the results are sorted by line, then type.
    """
    code = 'Public Function Foo(num)\n\nEnd Function\n'
    expected = [
        (1, "W400"),
        (2, "W400"),
        (3, "W400")
    ]
    linter = Linter()
    assert linter.lint(code) == expected
