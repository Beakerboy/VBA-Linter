from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.token_sequence_base import TokenSequenceBase
from typing import TypeVar


T = TypeVar('T', bound='MultipleSpacesComma')


class MultipleSpacesComma(TokenSequenceBase):
    def __init__(self: T) -> None:
        message = "Multiple spaces after ','"
        super().__init__("W241", [vbaLexer.T_0, vbaLexer.WS], 1, message)

    def match_action(self: T, token: Token) -> list:
        if len(token.text) > 1:
            line = token.line
            column = token.column
            name = self._rule_name
            return [(line, column + 1, name)]
        return []
