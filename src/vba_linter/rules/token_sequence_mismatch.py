from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenSequenceMismatch')


class TokenSequenceMismatch(RuleBase):
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
