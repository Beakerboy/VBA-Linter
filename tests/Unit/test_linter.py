import pytest
from vba_linter.linter import Linter


line_ending_data = [
    ('\r\n', []),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        [("W400", 2)]
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        [("W400", 1), ("W400", 2)]
    ),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: list) -> None:
    linter = Linter()
    assert linter.lint(code) == expected


eol_ws_data = [
    (
        'Public Function Foo(num) \r\nEnd Function\r\n',
        [("W200", 1)]
    ),
]


@pytest.mark.parametrize("code, expected", eol_ws_data)
def test_eol_ws(code: str, expected: list) -> None:
    linter = Linter()
    assert linter.lint(code) == expected

def test_sort() -> None
    """
    Test that the results are sorted by line, then type.
    """
    code = 'Public Function Foo(num) \n\nEnd Function \n'
    expected = [("W200", 1), ("W400", 1), ("W400", 2), ("W200", 3), ("W400", 3)]
    linter = Linter()
    assert linter.lint(code) == expected
