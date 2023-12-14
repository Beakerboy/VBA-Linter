from typing import TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    def __init__(self: T) -> None
        self.anti_patterns = []
        self.best_practice = []
        self.rule: RuleBase
    
    @pytest.mark.parametrize("code, expected",
                             self.anti_patterns + self.best_practice)
    def test_test(code: str, expected: list) -> None:
        linter = Linter()
        lexer = linter.get_lexer(code)
        tokens = lexer.getAllTokens()
        assert self.rule.test(tokens) == expected


    def test_message() -> None:
        data = (3, 13, "W291")
        expected = ":3:13: W291 trailing whitespace"
        assert self.rule.create_message(data) == expected
