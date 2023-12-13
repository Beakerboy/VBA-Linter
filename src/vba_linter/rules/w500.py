from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import Type, TypeVar


T = TypeVar('T', bound='W500')


class W500(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W500"
        self._line_ending = '\r\n'

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                newline_list = RuleBase.split_nl(token.text)
                num_nl = len(newline_list)
                for i in range(num_nl):
                    if newline_list[i] != self._line_ending:
                        column = token.column if i == 0 else 0
                        output.append((token.line + i, column, "W500"))
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return (output + 'Incorrect line ending')
