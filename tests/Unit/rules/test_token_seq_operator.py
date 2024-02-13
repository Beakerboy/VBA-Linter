import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_seq_operator import TokenSequenceOperator


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(2, 51, "001")]
    ]
]


rule = TokenSequenceOperator(
    "001",
    [vbaLexer.EQ, vbaLexer.WS, vbaLexer.LPAREN], 0,
    "Excess whitespace before '('")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
