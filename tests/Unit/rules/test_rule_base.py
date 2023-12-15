import pytest
from vba_linter.rules.rule_base import RuleBase


def test_constructor() -> None:
    base = RuleBase()
    assert isinstance(base, RuleBase)


def test_test() -> None:
    base = RuleBase()
    assert base.test([]) == []
