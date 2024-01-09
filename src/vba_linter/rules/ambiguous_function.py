from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='AmbiguousFunction')


class AmbiguousFunction(TokenSequenceBase):
    def __init__(self: T) -> None:
        self._rule_name = "E743"
        self._names = ['l', 'O', 'I']
        self._message = 'ambiguous function name'
        self._sequence = [vbaLexer.FUNCTION, vbaLexer.WS, vbaLexer.IDENTIFIER]
        self._target = 3

    def _match_action(self: T, token: Token) -> list:
        if token.text in self._names:
            return [(token.line, token.column + 1, self._rule_name)]
        return []
