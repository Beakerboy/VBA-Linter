import pytest
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory
from Unit.rule_stub import RuleStub


def test_constructor() -> None:
    obj = Linter()
    assert isinstance(obj, Linter)


def test_sort() -> None:
    """
    Test that the results are sorted by line, then char, type.
    """
    path = 'tests/Files/project/all_errors.bas'
    rule1 = RuleStub()
    rule1.set_name("E001")
    rule1.set_output([(1, 1, "E001"), (5, 5, "E001")])
    rule2 = RuleStub()
    rule2.set_name("E002")
    rule2.set_output([(1, 1, "E000"), (1, 4, "E002")])
    dir = RuleDirectory()
    dir.add_rule(rule1)
    dir.add_rule(rule2)
    expected = [
        (1, 1, "E000"), (1, 1, "E001"),
        (1, 4, "E002"), (5, 5, "E001")
    ]
    linter = Linter()
    assert linter.lint(dir, path) == expected


def test_not_file() -> None:
    linter = Linter()
    dir = RuleDirectory()
    with pytest.raises(Exception):
        linter.lint(dir, "foo.txt")


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
