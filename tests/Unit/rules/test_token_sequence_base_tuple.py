import pytest
from antlr4_vba.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.token_sequence_base import ToeknSequenceBase


anti_patterns = [
    [
        'Public Function Foo (num, bar)\r\nEnd Function\r\n',
        [(2, 20, "E203")]
    ]
]


rule = TokenSequenceBase("F00", ([vbaLexer.WS], [vbaLexer.LPAREN]), 1, )


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.tokenize(rule, code) == expected
