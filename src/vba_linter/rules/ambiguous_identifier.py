from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import List, TypeVar


T = TypeVar('T', bound='AmbiguousIdentifier')


class AmbiguousIdentifier(TokenSequenceBase):
    def __init__(self: T) -> None:
        self._rule_name = "E741"
        self._names = ['l', 'O', 'I']
        self._message = 'ambiguous variable name'
        self._sequence = [vbaLexer.IDENTIFIER]
        self._target = 0

    def _match_action(self: T, token: Token) -> list:
        if token.text in self._names:
            return [(token.line, token.column + 1, self._rule_name)]
        return []
