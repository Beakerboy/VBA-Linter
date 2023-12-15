import pytest
from vba_linter.linter import Linter


def test_constructor() -> None:
    obj = Linter()
    assert isinstance(obj, Linter)


def xtest_sort() -> None:
    """
    Test that the results are sorted by line, then type.
    """
    code = 'Public Function Foo(num) \n\nEnd Function \n'
    expected = [
        (1, 25, "W291"), (1, 25, "W500"),
        (2, 0, "W500"),
        (3, 13, "W291"), (3, 13, "W500")
    ]
    linter = Linter()
    assert linter.lint(code) == expected


name_formats = [
    ['snake_case', [True, False]],
    ['camelCase', [False, True]],
    ['PascalCase', [False, False]],
    ['hUngarian', [False, False]],
    ['kebab-case', [False, False]],
    ['i', [True, True]]
]


@pytest.mark.parametrize("name, expected", name_formats)
def test_snake_case(name: str, expected: list) -> None:
    assert Linter.is_snake_case(name) == expected[0]


@pytest.mark.parametrize("name, expected", name_formats)
def test_camel_case(name: str, expected: list) -> None:
    assert Linter.is_camel_case(name) == expected[1]
