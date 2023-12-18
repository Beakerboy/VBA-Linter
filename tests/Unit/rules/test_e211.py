import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rule_directory import RuleDirectory


anti_patterns = [
    [
        '''\
Public Function Foo (num)
End Function
''',  # noqa
        [(1, 20, "E211")]
    ],
    [
        '''\
Public Function Foo(data)
    bar = data (1)
End Function
''',  # noqa
        [(2, 15, "E211")]
    ],
]


message_data = [
    [(1, 20, "E211"), ":1:20: E211 whitespace before '('"],
 ]


rd = RuleDirectory()
rd.load_all_rules()
rule = rd.get_rule("E211")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "data, expected", message_data
)
def test_message(rule: RuleBase, data: tuple, expected: str) -> None:
    assert rule.create_message(data) == expected
