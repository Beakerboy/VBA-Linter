from vba_linter.rule_directory import RuleDirectory


def test_constructor() -> None:
    obj = RuleDirectory()
    assert isinstance(obj, RuleDirectory)
