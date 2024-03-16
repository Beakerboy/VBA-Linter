from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='AmbiguousIdentifier')


class AmbiguousIdentifier(TokenSequenceBase):
    def __init__(self: T) -> None:
        rule_name = "741"
        self._bad_names = ['l', 'O', 'I']
        message = 'ambiguous variable name'
        sequence = (
            [vbaLexer.IDENTIFIER, vbaLexer.WS, vbaLexer.AS],
            [vbaLexer.IDENTIFIER, vbaLexer.WS, vbaLexer.EQ]
        )
        target = 0
        super().__init__(rule_name, sequence, target, message)

    def _match_action(self: T, token: Token) -> list:
        if token.text in self._bad_names:
            return [(token.line, token.column + 1, self._rule_name)]
        return []
