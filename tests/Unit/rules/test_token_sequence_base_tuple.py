import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    [
        'Public Function Foo (num )\r\nEnd Function\r\n',
        [(1, 20, "F00"), (1, 25, "F00")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "F00")]
    ],
]


rule = TokenSequenceBase("F00",
                         (
                             [vbaLexer.IDENTIFIER, vbaLexer.WS, vbaLexer.LPAREN],
                             [vbaLexer.IDENTIFIER, vbaLexer.WS, vbaLexer.RPAREN]
                         ), 0,
                         "Whitespace before paren")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected
