import pytest
from antlr.vbaLexer import vbaLexer
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.token_after_base import TokenAfterBase


anti_patterns = [
    [
        'Public Function Foo( num)\r\nEnd Function\r\n',
        [(1, 21, "E201")]
    ],
    [
        'Foo = Bar( )\r\n',
        [(1, 11, "E201")]
    ],
]


rule = TokenAfterBase("E201",
                      vbaLexer.LPAREN, vbaLexer.WS,
                      "Whitespace after '('")


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    assert rule.test(tokens) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "E201")
    expected = ":3:13: E201 Whitespace after '('"
    assert rule.create_message(data) == expected
