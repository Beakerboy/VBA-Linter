from typing import Dict, List, TypeVar
from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.mixed_indent import MixedIndent
from vba_linter.rules.trailing_whitespace import TrailingWhitespace
from vba_linter.rules.newline_eof import NewlineEof
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from vba_linter.rules.blank_line_eof import BlankLineEof
from vba_linter.rules.line_ending import LineEnding
from vba_linter.rules.line_too_long import LineTooLong
from vba_linter.rules.parsing_error import ParsingError
from vba_linter.rules.listeners.optional_public import OptionalPublic
from vba_linter.rules.listeners.missing_visibility import MissingVisibility
from vba_linter.rules.listeners.missing_let import MissingLet
from vba_linter.rules.listeners.missing_module_attributes import (
    MissingModuleAttributes)


T = TypeVar('T', bound='RuleDirectory')


class RuleDirectory:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        self._rules: Dict[str, RuleBase] = {}
        self._parser_rules: Dict[str, ParseTreeListener] = {}

    def add_rule(self: T, rule: RuleBase) -> None:
        self._rules[rule.get_rule_name()] = rule

    def remove_rule(self: T, name: str) -> None:
        if name in self._rules:
            del self._rules[name]
        elif name in self._parser_rules:
            del self._parser_rules[name]

    def load_all_rules(self: T) -> None:
        symbols = [
            [vbaLexer.LPAREN, "(", (0, 0)],
            [vbaLexer.RPAREN, ")", (0, 0)],
            [vbaLexer.T__0, ',', (0, 1)],
            [vbaLexer.EQ, '=', (1, 1)],
            [vbaLexer.ASSIGN, ':=', (1, 1)],
        ]
        i = 1
        for symbol in symbols:
            self._rules.update(self._make_rules(symbol, i))
            i += 1

        self._rules.update({"W291": TrailingWhitespace(), "W201": NewlineEof(),
                            "W391": BlankLineEof(), "W500": LineEnding(),
                            "501": LineTooLong(), "101": MixedIndent()})
        self._parser_rules.update({
            'N100': OptionalPublic(),
            'N101': MissingVisibility(),
            'N102': MissingLet(),
            'N103': MissingModuleAttributes()
        })

    def get_rule(self: T, rule_name: str) -> RuleBase:
        if rule_name == "F999":
            return ParsingError()
        if rule_name not in self._rules:
            return RuleBase()
        return self._rules[rule_name]

    def get_parser_rules(self: T) -> List[ParseTreeListener]:
        lst = list(self._parser_rules.values())
        return lst

    def get_loaded_rules(self: T) -> dict:
        return self._rules

    def _make_rules(self: T, symbol: list, index: int) -> dict:
        rules: Dict[str, RuleBase] = {}
        i = 10 * index + 120
        token = symbol[0]
        name = symbol[1]
        number = symbol[2]
        # Currently only worrying about 0 or 1
        if number[0] == 0:
            # No "missing" rule.
            i += 1
            rules[str(i)] = TokenSequenceBase(
                str(i),
                [vbaLexer.WS, token], 0,
                "Excess whitespace before '" + name + "'")
        elif number[0] == 1:
            rules[str(i)] = TokenSequenceMismatch(
                str(i),
                [vbaLexer.WS, token], 0,
                "Missing whitespace before " + name)
            i += 1
            # todo: create "excess whitespace" rule.
        i += 1
        # check if preceeding whitespace contains tabs.
        i += 1
        if number[0] == 0:
            # No "missing" rule.
            i += 1
            rules[str(i)] = TokenSequenceBase(
                str(i),
                [token, vbaLexer.WS], 1,
                "Excess whitespace after '" + name + "'")
        elif number[1] == 1:
            rules[str(i)] = TokenSequenceMismatch(
                str(i),
                [token, vbaLexer.WS], 1,
                "Missing whitespace after '" + name + "'")
            i += 1
            # todo: create "excess whitespace" rule.
        return rules
