import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.ws_contains import WsContains


anti_patterns = [
    [
        '''\
Public Function Foo(num)
\tBar = 2
End Function
''',  # noqa
        [(2, 1, "100:200")]
    ],
]


message_data = [
    [(2, 1, "100:200"), ":2:1: E200 Indentation contains tabs"],
 ]


rule = WsContains()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "data, expected", message_data
)
def test_message(rule: RuleBase, data: tuple, expected: str) -> None:
    assert rule.create_message(data) == expected
