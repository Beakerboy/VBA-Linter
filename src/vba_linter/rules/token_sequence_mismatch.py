from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TokenSequenceMismatch')


class TokenSequenceMismatch(TokenSequenceBase):
    """
    create an error if a seqenece matches all tokens,
    but must be not equal at the specified position.
    """
    def _match_action(self: T, token: Token) -> list:
        line = token.line
        if self._target == 1:
            column = token.column + len(token.text)
        elif self._target == 2:
            column = token.column
        name = self._rule_name
        return [(line, column + 1, name)]

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        result = True
        for i in range(len(sequence)):
            if i == self._target - 1:
                result = result and (
                    sequence[i] != signature[i] or (
                        signature[i] == vbaLexer.WS and
                        sequence[i] == vbaLexer.LINE_CONTINUATION
                    )
                )
            else:
                result = result and sequence[i] == signature[i]
        return result
