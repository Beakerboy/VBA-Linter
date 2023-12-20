from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


class TokenBeforeBase(RuleBase):
    def __init__(self: T, name: str,
                 first: int, second: int,
                 message: str) -> None:
        self._rule_name = name
        self._token_second = second
        self._token_first = first
        self._message = message

    def test(self: T, lexer: vbaLexer) -> list:
        tokens = lexer.getAllTokens()
        output: list[tuple] = []
        if len(tokens) < 2:
            return output
        prev_tok = tokens[0]
        for token in tokens[1:]:
            if (prev_tok.type == self._token_first and
                    token.type == self._token_second):
                line = token.line
                column = token.column
                name = self._rule_name
                output.append((line, column, name))
            prev_tok = token
        return output
