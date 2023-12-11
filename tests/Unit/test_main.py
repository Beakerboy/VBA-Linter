import pytest
from vba_linter.__main__ import main


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
    argv = ["main", code]
    assert main(argv) == expected
