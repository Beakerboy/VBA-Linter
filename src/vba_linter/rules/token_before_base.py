from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenBeforeBase')


class TokenBeforeBase(RuleBase):

    def test(self: T, tokens: list) -> list:
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            if token.type == self._token_find:
                if not (prev_tok is None) and prev_tok.type == self._token_bad:
                    output.append((token.line, token.column, self._rule_name))
            prev_tok = token
        return output
