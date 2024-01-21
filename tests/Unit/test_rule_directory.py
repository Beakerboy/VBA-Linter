from vba_linter.rule_directory import RuleDirectory
from Unit.rule_stub import RuleStub


def test_constructor() -> None:
    obj = RuleDirectory()
    assert isinstance(obj, RuleDirectory)


def test_add_and_remove() -> None:
    obj = RuleDirectory()
    rule1 = RuleStub()
    rule1.set_name("001")
    assert len(obj.get_loaded_rules()) == 0
    obj.add_rule(rule1)
    assert len(obj.get_loaded_rules()) == 1
    obj.remove_rule("001")
    assert len(obj.get_loaded_rules()) == 0
