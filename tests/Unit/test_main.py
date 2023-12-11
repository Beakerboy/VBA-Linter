import pytest
from vba_linter.__main__ import main


line_ending_data = [
    (
        'Public Function Foo(num)\nEnd Function',
        "line: 1 incorrect line ending\n"
    ),
    ('\r\n', ""),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: str) -> None:
    argv = ["main", code]
    assert main(argv) == expected
