import pytest
from vba_linter.linter import Linter


line_ending_data = [
    ('\r\n', []),
    ('Function Foo()\r\n\r\nEnd Function\r\n', []),
    ('\n\r\nFunction Foo()\r\n\r\nEnd Function\r\n', [(1, "W500")]),
    ('\r\n\nFunction Foo()\r\n\r\nEnd Function\r\n', [(2, "W500")]),
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


def test_no_newline() -> None:
    code = 'Public Function Foo(num)\r\nEnd Function'
    linter = Linter()
    assert linter.lint(code) == [(2, "W201")]


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


extra_eol = [
    [
        'Public Function Foo(num)\r\nEnd Function\r\n\r\n',
        [(3, "W300")]
    ],
    [
        'Public Function Foo(num)\r\nEnd Function\r\n\r\n\r\n',
        [(3, "W300"), (4, "W300")]
    ]
]


@pytest.mark.parametrize("name, expected", extra_eol)
def test_extra_end_lines(code: str, expected: list) -> None:
    linter = Linter()
    assert linter.lint(code) == expected
