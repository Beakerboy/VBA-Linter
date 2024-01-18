from antlr4 import Token
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TokenLengthMismatch')


class TokenLengthMismatch(TokenSequenceBase):

    def _match_action(self: T, token: Token) -> list:
        if len(token.text) > 1:
            line = token.line
            column = token.column
            name = self._rule_name
            return [(line, column + 1, name)]
        return []
