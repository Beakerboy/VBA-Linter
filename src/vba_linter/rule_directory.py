from typing import Dict, List, TypeVar
from antlr4 import ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.mixed_indent import MixedIndent
from vba_linter.rules.trailing_whitespace import TrailingWhitespace
from vba_linter.rules.newline_eof import NewlineEof
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from vba_linter.rules.token_seq_mismatch_nl import TokenSeqMismatchNL
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from vba_linter.rules.token_seq_operator import TokenSequenceOperator
from vba_linter.rules.token_length_mismatch import TokenLengthMismatch
from vba_linter.rules.blank_line_eof import BlankLineEof
from vba_linter.rules.blank_line_ws import BlankLineWhitespace
from vba_linter.rules.blank_line_number import BlankLineNumber
from vba_linter.rules.line_ending import LineEnding
from vba_linter.rules.line_too_long import LineTooLong
from vba_linter.rules.parsing_error import ParsingError
from vba_linter.rules.keyword_caps import KeywordCaps
from vba_linter.rules.listeners.optional_public import OptionalPublic
from vba_linter.rules.listeners.missing_visibility import MissingVisibility
from vba_linter.rules.listeners.missing_let import MissingLet
from vba_linter.rules.listeners.optional_let import OptionalLet
from vba_linter.rule_disabler import RuleDisabler


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
        if isinstance(rule, ParseTreeListener):
            self._parser_rules[rule.get_rule_name()] = rule
        else:
            self._rules[rule.get_rule_name()] = rule

    def remove_rule(self: T, name: str) -> None:
        if name in self._rules:
            del self._rules[name]
        elif name in self._parser_rules:
            del self._parser_rules[name]

    def load_standard_rules(self: T) -> None:
        symbols = [
            [vbaLexer.LPAREN, "(", ('s', 0)],
            [vbaLexer.RPAREN, ")", (0, 's')],
            [vbaLexer.COMMA, ',', (0, 1)],
            [vbaLexer.EQ, '=', (1, 1)],
            [vbaLexer.ASSIGN, ':=', (0, 0)],
        ]
        i = 1
        for symbol in symbols:
            self._rules.update(self._make_rules(symbol, i))
            i += 1
        rule910 = LineTooLong(1023)
        rule910.set_rule_name("910")
        rule910.severity = 'F'
        self._rules.update({
            "201": NewlineEof(),
            "220": KeywordCaps(),
            "400": LineEnding(),
            "305": TrailingWhitespace(),
            "910": rule910
        })
        self.add_rule(RuleDisabler())

    def load_all_rules(self: T) -> None:
        self.load_standard_rules()

        self._rules.update({
            "391": BlankLineEof(), "303": BlankLineNumber(),
            "310": BlankLineWhitespace(),
            "501": LineTooLong(), "101": MixedIndent()
        })
        self._parser_rules.update({
            '505': OptionalPublic(),
            '510': MissingVisibility(),
            '110': MissingLet(), '111': OptionalLet()
        })

    def get_rule(self: T, rule_name: str) -> RuleBase:
        if rule_name == "999":
            return ParsingError()
        if rule_name in self._rules:
            return self._rules[rule_name]
        elif (
            rule_name in self._parser_rules and
            isinstance(self._parser_rules[rule_name], RuleBase)
        ):
            rule = self._parser_rules[rule_name]
            assert isinstance(rule, RuleBase)
            return rule
        else:
            return RuleBase()

    def get_parser_rules(self: T) -> List[ParseTreeListener]:
        lst = list(self._parser_rules.values())
        return lst

    def get_loaded_rules(self: T) -> dict:
        return self._rules

    def _make_rules(self: T, symbol: list, index: int) -> dict:
        rules: Dict[str, RuleBase] = {}
        i = 10 * index + 110
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
                "Missing whitespace before '" + name + "'")
            i += 1
            rules[str(i)] = TokenLengthMismatch(
                str(i),
                [vbaLexer.WS, token], 0,
                "Excess whitespace before '" + name + "'"
            )
        elif number[0] == 's':
            i += 1
            rules[str(i)] = TokenSequenceOperator(
                str(i),
                [vbaLexer.EQ, vbaLexer.WS, token], 0,
                "Excess whitespace before '" + name + "'")
        i += 1
        # check if preceeding whitespace contains tabs.
        i += 1
        if number[1] == 0:
            # No "missing" rule.
            i += 1
            rules[str(i)] = TokenSequenceBase(
                str(i),
                [token, vbaLexer.WS], 1,
                "Excess whitespace after '" + name + "'")
        elif number[1] == 1 or number[1] == 's':
            if number[1] == 1:
                rules[str(i)] = TokenSequenceMismatch(
                    str(i),
                    [token, vbaLexer.WS], 1,
                    "Missing whitespace after '" + name + "'")
            else:
                """
                We need to carve out an exception for a newline
                following an rparen
                """
                rules[str(i)] = TokenSeqMismatchNL(
                    str(i),
                    [token, vbaLexer.WS], 1,
                    "Missing whitespace after '" + name + "'")
            i += 1
            rules[str(i)] = TokenLengthMismatch(
                str(i),
                [token, vbaLexer.WS], 1,
                "Excess whitespace after '" + name + "'"
            )
        return rules
