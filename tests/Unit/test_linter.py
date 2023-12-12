import pytest
from vba_linter.linter import Linter


line_ending_data = [
    ('\r\n', []),
    ('\r\n\r\n', []),
    ('\n\r\n', [(1, "W500")]),
    ('\r\n\n', [(2, "W500")]),
    ('\r\n\r\nFoo\n', [(3, "W500")]),
    (
        'Public Function Foo(num)\r\nEnd Function\n',
        [(2, "W500")]
    ),
    (
        'Public Function Foo(num)\nEnd Function\n',
        [(1, "W500"), (2, "W500")]
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
    code = 'Public Function Foo(num) \n\nEnd Function \n'
    expected = [
        (1, "W200"), (1, "W500"),
        (2, "W500"),
        (3, "W200"), (3, "W500")
    ]
    linter = Linter()
    assert linter.lint(code) == expected


name_formats = [
    ['snake_case', [True, False]],
    ['camelCase', [False, True]],
    ['PascalCase', [False, False]],
    ['hUngarian', [False, False]],
    ['camelsnake', [True, True]]
]


@pytest.mark.parametrize("name, expected", name_formats)
def test_snake_case(name: str, expected: list) -> None:
    assert Linter.is_snake_case(name) == expected[0]


@pytest.mark.parametrize("name, expected", name_formats)
def test_camel_case(name: str, expected: list) -> None:
    assert Linter.is_camel_case(name) == expected[1]
