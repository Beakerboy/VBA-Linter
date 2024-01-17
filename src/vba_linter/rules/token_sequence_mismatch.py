from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='TokenSequenceMismatch')


class TokenSequenceMismatch(TokenSequenceBase):
    """
    Create an error if the stream mathes a given sequence
    of token types.
    """

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        result = True
        for i in range(len(sequence)):
            if i != self._target:
                result = result and sequence[i] == signature[i]
        return result
