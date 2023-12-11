import pytest
from vba_linter.__main__ import main

err = "line: " + "incorrect line ending"


line_ending_data = [
    ('Public Function Foo(num)\nEnd Function', err),
    ('\r\n', None),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: str) -> None:
    argv = ["main", code]
    assert main(argv) == expected
