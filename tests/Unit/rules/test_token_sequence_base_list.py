import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_sequence_base import TokenSequenceBase


anti_patterns = [
    [
        'Attribute VB_Name = "Foo"\r\nPublic Function Foo(num )\r\nEnd Function\r\n',
        [(2, 24, "E202")]
    ],
    [
        'Attribute VB_Name = "Foo"\r\nFoo = Bar( )\r\n',
        [(2, 11, "E202")]
    ],
]


rule = TokenSequenceBase("E202",
                         [vbaLexer.WS, vbaLexer.RPAREN], 0,
                         "Whitespace before ')'")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
