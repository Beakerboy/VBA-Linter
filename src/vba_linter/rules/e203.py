from antlr.vbaLexer import vbaLexer
from vba_linter.rules.token_before_base import TokenBeforeBase
from typing import TypeVar


T = TypeVar('T', bound='E203')


class E203(TokenBeforeBase):
    def __init__(self: T) -> None:
        self._rule_name = "E203"
        self._token_find = vbaLexer.T__0
        self._token_bad = vbaLexer.WS
        self._message = "Whitespace before ','"
        # self._find_value = ','
        self._find_value = ''

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        for token in tokens:
            line = token.line
            column = token.column
            name = token.type
            text = token.text
            output.append((line, column, name, text))
        return output
