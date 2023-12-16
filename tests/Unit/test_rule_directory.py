from vba_linter.rule_directory import RuleDirectory
from Unit.rule_stub import RuleStub
from vba_linter.linter import Linter


def test_constructor() -> None:
    obj = RuleDirectory()
    assert isinstance(obj, RuleDirectory)


def test_add() -> None:
    obj = RuleDirectory()
    rule1 = RuleStub()
    obj.add_rule(rule1)
    obj.test_all()
    assert rule1.test_count == 1
    rule2 = RuleStub()
    obj.add_rule(rule2)

    code = ""
    linter = Linter()
    obj.test_all(linter.get_lexer(code).getAllTokens())
    assert rule1.test_count == 2
    assert rule2.test_count == 1
