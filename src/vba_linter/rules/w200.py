from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W200')


class W200(RuleBase):
    def __init__(self: T) -> None:
        self._rule_name = "W200"
        self._token_find = vbaLexer.NEWLINE
        self._token_bad = vbaLexer.WS

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            if token.type == self._token_find:
                if not (prev_tok is None) and prev_tok.type == self._token_bad:
                    output.append((token.line, token.column, self._rule_name))
            prev_tok = token
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + "Unexpected whitespace at the end of the line"
