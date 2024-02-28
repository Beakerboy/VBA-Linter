from antlr4 import CommonTokenStream, Token
from vba_linter.rules.rule_base import RuleBase
from typing import List, Tuple, TypeVar, Union


T = TypeVar('T', bound='TokenSequenceBase')


class TokenSequenceBase(RuleBase):
    """
    Create an error if the stream mathes a given sequence
    of token types.
    """
    def __init__(self: T, name: str,
                 sequence: Union[List[int], Tuple[List[int], ...]],
                 target: int, message: str) -> None:
        """
        if sequence is passed in as a tuple, and the contained lists have
        different lengths, the shorted list must be first to prevent
        an early return.
        """
        super().__init__()
        self._rule_name = name
        self._sequence = sequence

        # The element who's position is reported
        self._target = target + 1
        self._message = message
        # what is a good initial value...what value is unused in the Lexer?
        self.exception: int = -1

    def test(self: T, ts: CommonTokenStream) -> list:
        """
        extract the sequence of tokens at the current position
        """
        output: List[tuple] = []
        sequences: Tuple[List[int], ...]
        if isinstance(self._sequence, list):
            sequences = (self._sequence, )
        else:
            sequences = self._sequence
        for sequence in sequences:
            found_eof = False
            token_types: List[int] = []
            seq_len = len(sequence)
            for i in range(seq_len):
                if found_eof:
                    return output
                tok_type = ts.LA(i + 1)
                if tok_type == Token.EOF:
                    found_eof = True
                token_types.append(tok_type)
            if (
                    self.match(token_types, sequence) and
                    (
                        self.exception == -1 or
                        self.exception != -1 and
                        ts.LA(seq_len + 1) != self.exception
                    )
            ):
                token = ts.LT(self._target)
                assert token is not None
                output = self._match_action(token)
        return output

    def _match_action(self: T, token: Token) -> list:
        line = token.line
        column = token.column
        name = self._rule_name
        return [(line, column + 1, name)]

    def match(self: T, sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        return sequence == signature
