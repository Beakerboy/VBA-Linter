from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenBetweenBase')


class TokenBetweenBase(RuleBase):
    def __init__(self: T, name: str,
                 first: int, second: int,
                 third: int, message: str) -> None:
        self._rule_name = name
        self._token_second = second
        self._token_first = first
        self._token_third = third
        self._message = message

    def test(self: T, lexer: vbaLexer) -> list:
        tokens = lexer.getAllTokens()
        output: list[tuple] = []
        if len(tokens) < 3:
            return output
        tok1 = tokens[0]
        tok2 = tokens[1]
        for token in tokens[2:]:
            if (token.type == self._token_third and
                    tok1.type == self._token_first and
                    tok2.type == self._token_second):
                line = token.line
                column = token.column
                name = self._rule_name
                output.append((line, column, name))
            tok1 = tok2
            tok2 = token
        return output
