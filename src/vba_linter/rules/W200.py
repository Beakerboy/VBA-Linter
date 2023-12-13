from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar

T = TypeVar('T', bound='W200')

class W200(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W200"

    def test(self: T, tokens: list) -> list:
        output = []
        prev_tok = None
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if not (prev_tok is None) and prev_tok.type == vbaLexer.WS:
                    output.append((token.line, "W200"))
            prev_tok = token
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return output + "Unexpected whitespace at the end of the line"
