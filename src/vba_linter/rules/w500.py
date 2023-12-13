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
                newline_list = W500.split_nl(token.text)
                num_nl = len(newline_list)
                for i in range(num_nl):
                    if newline_list[i] != self._line_ending:
                        output.append((token.line + i, "W500"))
        return output

    def create_message(self: T, data: tuple) -> str:
        output = RuleBase.create_message(self, data)
        return (output + 'Incorrect line ending')

    @classmethod
    def split_nl(cls: Type[T], nl: str) -> list:
        """
        split a newline token into separate line end characters.
        """
        num = len(nl)
        i = 0
        result = []
        while i < num:
            if num >= 2 and nl[i:i+2] == '\r\n':
                result.append('\r\n')
                i += 2
            else:
                result.append(nl[i:i+1])
                i += 1
        return result
