import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w501 import W501


anti_patterns = [
    ['''\
Public Function Supercalifragilisticexpialidocious(atrocious, precocious, indubitably)
End Function
''',  # noqa
     [(1, 86, 'W501')]
    ]
]


rule = W501()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    RuleTestBase.test_test(rule, code, expected)


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 86, "W501")
    expected = ":3:86: W501 incorrect line ending"
    assert rule.create_message(data) == expected
