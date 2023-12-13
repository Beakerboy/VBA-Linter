import pytest
from vba_linter.linter import Linter


def test_sort() -> None:
    """
    Test that the results are sorted by line, then type.
    This should be modified to use RuleStub. 
    """
    code = 'Public Function Foo(num) \n\nEnd Function \n'
    expected = [
        (1, 25, "W200"), (1, 25, "W500"),
        (2, 0, "W500"),
        (3, 13, "W200"), (3, 13, "W500")
    ]
    linter = Linter()
    assert linter.lint(code) == expected


bad_code = [
    ['<?php phpinfo(); ?>'],
    ['Function Foo()\r\nEnd Sub\r\n']
]   

@pytest.mark.parametrize("code", bad_code)
def test_bad_file(code: str) -> None:
    """
    Something bad should happen if the code cannot parse
    """
    linter = Linter()
    assert linter.lint(code) == []


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
