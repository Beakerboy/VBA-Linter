import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.token_sequence_base import ToeknSequenceBase
from vba_linter.rules.rule_base import RuleBase


anti_patterns = [
    [
        'Public Function Foo(num )\r\nEnd Function\r\n',
        [(1, 24, "E202")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "E202")]
    ],
]


rule = TokenSequenceBase("E202",
                         ([vbaLexer.WS], [vbaLexer.RPAREN]), 0,
                         "Whitespace before ')'")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected
