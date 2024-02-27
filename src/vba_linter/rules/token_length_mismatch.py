from antlr4 import Token
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TokenLengthMismatch')


class TokenLengthMismatch(TokenSequenceBase):
    """
    if a sequence of tokens matches the target, check that the
    matching token has the idicated length.
    """
    def _match_action(self: T, token: Token) -> list:
        max = 1
        text = token.text.replace("\t", " " * 8)
        if len(text) > max:
            line = token.line
            column = token.column
            name = self._rule_name
            return [(line, column + 1 + max, name)]
        return []
