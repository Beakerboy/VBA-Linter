import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_length_mismatch import TokenLengthMismatch


anti_patterns = [
    [
        'Public Function Foo(num,mum)\r\nEnd Function\r\n',
        [(1, 25, "B83")]
    ]
]


rule = TokenLengtgMismatch(
    "B83", [vbaLexer.T__0, vbaLexer.WS], 1, "Whitespace after ','"
)


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected
