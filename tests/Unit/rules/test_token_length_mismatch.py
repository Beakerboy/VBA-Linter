import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_length_mismatch import TokenLengthMismatch


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(5, 3, "303"),
         (7, 16, "303")]
    ]
]


rule = TokenLengthMismatch(
    "303",
    [vbaLexer.WS, vbaLexer.EQ], 0,
    "Excess whitespace before '='"
)


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
