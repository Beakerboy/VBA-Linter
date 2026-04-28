import pytest
from vba_linter.rules.vbalistener_test_runner import VbaListenerTestRunner


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
    assert VbaListenerTestRunner.is_snake_case(name) == expected[0]


@pytest.mark.parametrize("name, expected", name_formats)
def test_camel_case(name: str, expected: list) -> None:
    assert VbaListenerTestRunner.is_camel_case(name) == expected[1]
