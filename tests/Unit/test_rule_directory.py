from vba_linter.rule_directory import RuleDirectory
from Unit.rule_stub import RuleStub

def test_constructor() -> None:
    obj = RuleDirectory()
    assert isinstance(obj, RuleDirectory)

def test_add() -> None:
    obj = RuleDirectory()
    rule = RuleStub()
    a = len(obj.get_rules())
    obj.add_rule(rule)
    assert len(obj.get_rules()) == a + 1
