from typing import Dict, TypeVar
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
# from vba_linter.rules.mixed_indent import MixedIndent
# from vba_linter.rules.trailing_whitespace import TrailingWhitespace
# from vba_linter.rules.newline_eof import NewlineEof
# from vba_linter.rules.token_after_base import TokenAfterBase
from vba_linter.rules.token_before_base import TokenBeforeBase
# from vba_linter.rules.token_between_base import TokenBetweenBase
# from vba_linter.rules.blank_line_eof import BlankLineEof
# from vba_linter.rules.line_ending import LineEnding
# from vba_linter.rules.line_too_long import LineTooLong
from vba_linter.rules.parsing_error import ParsingError


T = TypeVar('T', bound='RuleDirectory')


class RuleDirectory:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules: Dict[str, RuleBase] = {}

    def add_rule(self: T, rule: RuleBase) -> None:
        self._rules[rule.get_rule_name()] = rule

    def load_all_rules(self: T) -> None:
        """
        e201 = TokenAfterBase("E201",
                              vbaLexer.LPAREN, vbaLexer.WS,
                              "Whitespace after '('")
        """
        e202 = TokenBeforeBase("E202",
                               vbaLexer.WS, vbaLexer.RPAREN,
                               "Whitespace before ')'")
        e203 = TokenBeforeBase("E203",
                               vbaLexer.WS, vbaLexer.T__0,
                               "Whitespace before ','")
        """
        e211 = TokenBetweenBase("E211", vbaLexer.IDENTIFIER, vbaLexer.WS,
                                vbaLexer.LPAREN, "whitespace before '('")

        self._rules.update({"E201": e201, "E202": e202, "E203": e203,
                            "E211": e211})
        """
        self._rules.update({"E202": e202, "E203": e203})
        """
        self._rules.update({"W291": TrailingWhitespace(), "W201": NewlineEof(),
                            "W391": BlankLineEof(), "W500": LineEnding(),
                            "W501": LineTooLong(), "E101": MixedIndent()})
        """
    def get_rule(self: T, rule_name: str) -> RuleBase:
        if rule_name == "E999":
            return ParsingError()
        return self._rules[rule_name]

    def get_loaded_rules(self: T) -> dict:
        return self._rules
