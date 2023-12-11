import pytest
from vba_linter.__main__ import main

err = "line: " + "incorrect line ending"


line_ending_data = [
    ('\n', err),
    ('\r\n', ''),
]


@pytest.mark.parametrize("code, expected", line_ending_data)
def test_line_ending(code: str, expected: str) -> None:
    argv = ["main", code]
    assert main(argv) == expected
