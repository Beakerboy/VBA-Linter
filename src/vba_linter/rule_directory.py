from typing import TypeVar
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.w291 import W291
from vba_linter.rules.w201 import W201
from vba_linter.rules.token_after_base import TokenAfterBase
from vba_linter.rules.token_before_base import TokenBeforeBase
from vba_linter.rules.token_between_base import TokenBetweenBase
from vba_linter.rules.w391 import W391
from vba_linter.rules.w500 import W500
from vba_linter.rules.w501 import W501
from vba_linter.rules.e999 import E999


T = TypeVar('T', bound='RuleDirectory')


class RuleDirectory:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules: dict[str, RuleBase] = {}

    def add_rule(self: T, rule: RuleBase) -> None:
        self._rules[rule.get_rule_name()] = rule

    def load_all_rules(self: T) -> None:
        e201 = TokenAfterBase("E201",
                              vbaLexer.LPAREN, vbaLexer.WS,
                              "Whitespace after '('")
        e202 = TokenBeforeBase("E202",
                               vbaLexer.WS, vbaLexer.RPAREN,
                               "Whitespace before ')'")
        e203 = TokenBeforeBase("E203",
                               vbaLexer.WS, vbaLexer.T__0,
                               "Whitespace before ','")
        e211 = TokenBetweenBase("E211", vbaLexer.IDENTIFIER, vbaLexer.WS,
                                vbaLexer.LPAREN, "whitespace before '('")
        self._rules.update({"E201": e201, "E202": e202, "E203": e203,
                            "E211": e211})
        self._rules.update({"W291": W291(), "W201": W201(),
                            "W391": W391(), "W500": W500(),
                            "W501": W501()})

    def get_rule(self: T, rule_name: str) -> RuleBase:
        if rule_name == "E999":
            return E999()
        return self._rules[rule_name]

    def get_loaded_rules(self: T) -> dict:
        return self._rules
