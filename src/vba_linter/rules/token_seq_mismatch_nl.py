from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from typing import TypeVar


T = TypeVar('T', bound='TokenSeqMismatchNL')


class TokenSeqMismatchNL(TokenSequenceMismatch):
    """
    create an error is a seqenece matches all tokens,
    but mist be not equal at the specified position.
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
        sequence is the list of tokens from the stream
        signature is the 'target'
        """
        result = True
        for i in range(len(sequence)):
            if i == self._target - 1:
                result = result and (
                    sequence[i] != signature[i] or 
                    sequence[i] == vbaLexer.NEWLINE
                )
            else:
                result = result and sequence[i] == signature[i]
        return result
