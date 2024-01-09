from antlr4 import CommonTokenStream, Token
from vba_linter.rules.rule_base import RuleBase
from typing import Collection, List, Type, TypeVar


T = TypeVar('T', bound='TokenSequenceBase')


class TokenSequenceBase(RuleBase):
    """
    Create an error if the stream mathes a given sequence
    of token types.
    """
    def __init__(self: T, name: str,
                 sequence: Collection, target: int,
                 message: str) -> None:
        self._rule_name = name
        self._sequence = sequence

        # The element who's position is reported
        self._target = target + 1
        self._message = message

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token_types: list = []
        found_eof = False
        if type(self._sequence) is not set:
            sequences = {self._sequence}
        else sequences = self._sequence
        for sequence in sequences:
            for i in range(len(sequence)):
                if found_eof:
                    return output
                tok_type = ts.LA(i + 1)
                if tok_type == Token.EOF:
                    found_eof = True
                token_types.append(tok_type)
        if TokenSequenceBase.match(token_types, self._sequence):
            token = ts.LT(self._target)
            output = self._match_action(token)
        return output

    def _match_action(self: T, token: Token) -> list:
        line = token.line
        column = token.column
        name = self._rule_name
        return [(line, column + 1, name)]

    @classmethod
    def match(cls: Type[T], sequence: list, signature: list) -> bool:
        """
        Compare the two lists to see if they match.
        """
        return sequence == signature
