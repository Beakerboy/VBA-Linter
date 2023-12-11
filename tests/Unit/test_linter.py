import pytest
from vba_linter.linter import Linter


line_ending_data = [
    ('\r\n', ""),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        "line: 2 incorrect line ending\n"
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        "line: 1 incorrect line ending\nline: 2 incorrect line ending\n"
    ),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: str) -> None:
    linter = Linter()
    assert linter.lint(code) == expected


eol_ws_data = [
    (
        'Public Function Foo(num) \r\nEnd Function\r\n',
        "line: 1 trailing whitespace\n"
    ),
]


@pytest.mark.parametrize("code, expected", eol_ws_data)
def test_eol_ws(code: str, expected: str) -> None:
    linter = Linter()
    assert linter.lint(code) == expected
