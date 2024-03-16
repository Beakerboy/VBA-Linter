from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_mismatch import TokenSequenceMismatch
from typing import TypeVar


T = TypeVar('T', bound='TokenSeqMismatchNL')


class TokenSeqMismatchNL(TokenSequenceMismatch):
    """
    create an error is a seqenece matches all tokens,
    but mist be not equal at the specified position.
    """

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        sequence is the list of tokens from the stream
        signature is the 'target'
        """
        result = super().match(sequence, signature)
        exceptions = [vbaLexer.RPAREN, vbaLexer.LPAREN, vbaLexer.NEWLINE,
                      vbaLexer.COMMA, vbaLexer.PERIOD, vbaLexer.COLON,
                      vbaLexer.SEMICOLON]
        return result and sequence[1] not in exceptions
