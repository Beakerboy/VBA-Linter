from antlr.vbaLexer import vbaLexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='W300')


class W300(RuleBase):
    def __init__(self: T) -> None:
        self.rule_name = "W300"

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        final_token = tokens[-1]
        if final_token.type == vbaLexer.NEWLINE:
            newline_list = RuleBase.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                for i in range(num_nl - 1):
                    output.append((final_token.line + i + 1, "W300"))
        return output
