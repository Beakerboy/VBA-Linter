from vba_linter.rule_loader import RuleLoader


def test_constructor() -> None:
    obj = RuleLoader()
    assert isinstance(obj, RuleLoader)
