import pytest
from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from Unit.token_stream_stub import TokenStreamStub
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.line_ending import LineEnding


anti_patterns = [
    (
        RuleTestBase.worst_practice,
        [
            (2, 92, "400"),
            (3, 0, "400"),
            (6, 11, "400"),
            (9, 12, "400")
        ]
    )
]


rule = LineEnding()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


@pytest.mark.parametrize('rule', [rule])
def test_message(rule: RuleBase) -> None:
    data = (3, 13, "400")
    expected = ":3:13: E400 incorrect line ending"
    assert rule.create_message(data) == expected


def test_custom_streams() -> None:
    tok = Token()
    tok.type = vbaLexer.NEWLINE
    tok.line = 1
    tok.column = 0
    tok.text = "\n"
    ts = TokenStreamStub([tok])
    assert rule.test(ts) == (1, 0, '400')
