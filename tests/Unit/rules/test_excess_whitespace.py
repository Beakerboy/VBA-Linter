import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase
from vba_linter.rules.excess_whitespace import ExcessWhitespace


anti_patterns = [
    [
        '''\
Attribute VB_Name = "Foo"
Public Function Foo( num )
    Bar 2, 3 , 4, baz := 5
label1 : x  =  2
End Function
''',  # noqa
        [
            (2, 21, "151:124", 'after', '('),
            (2, 25, "151:131", 'before', ')'),
            (3, 13, "151:141", 'before', ','),
            (3, 22, "151:161", 'before', ':='),
            (3, 25, "151:164", 'after', ':='),
            (4, 7, "151:191", 'before', ':'),
            (4, 12, "151:151", 'before', '='),
            (4, 15, "151:154", 'after', '=')
        ]
    ]
]


message_data = [
    [
        (3, 1, "151:124", 'before', ')'),
        ":3:1: E124 Excess whitespace before ')'"
    ],
 ]


rule = ExcessWhitespace()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: ListenerRuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_combo_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "data, expected", message_data
)
def test_message(rule: ListenerRuleBase, data: tuple, expected: str) -> None:
    assert rule.create_message(data) == expected
