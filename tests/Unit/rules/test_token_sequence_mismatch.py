import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch


anti_patterns = [
    [
        'Public Function Foo(num,mum)\r\nEnd Function\r\n',
        [(1, 25, "B83")]
    ]
]


rule = TokenSequenceMismatch(
    "B83", [vbaLexer.COMMA, vbaLexer.WS], 1, "Whitespace after ','"
)


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected
