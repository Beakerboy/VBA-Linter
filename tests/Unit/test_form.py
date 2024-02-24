from pytest_mock import MockerFixture
from vba_linter.linter import Linter
from vba_linter.rule_directory import RuleDirectory


def test_form(mocker: MockerFixture) -> None:
    dir = RuleDirectory()
    linter = Linter()
    file_name = "tests/files/login.frm"
    dir.load_all_rules()
    dir.remove_rule("400")
    results = linter.lint(dir, file_name)
    assert len(results) == 13
    rule_disabler = dir.get_rule_disabler()
    ignored_lines = rule_disabler.ignored
    assert "151" in ignored_lines
    assert "154" in ignored_lines
    for line_num in range(3, 9):
        assert line_num in ignored_lines["151"]
        assert line_num in ignored_lines["154"]