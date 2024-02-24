from pytest_mock import MockerFixture
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def test_form(mocker: MockerFixture) -> None:
    dir = RuleDirectory()
    dir.load_standard_rules()
    results = linter.lint(dir, file_name)
    rule_disabler = dir.get_rule_disabler()
