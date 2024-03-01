from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from typing import List, TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='ExcessWhitespace')


class ExcessWhitespace(RuleBase):

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        seq = self._build_list(ts, 3)
        # Tokens which must have no whiteapace after.
        pre_single_ws = [vbaLexer.ASSIGN]
        # Tokens which must have no whitespace before.
        post_single_ws = [vbaLexer.COLON, vbaLexer.ASSIGN, vbaLexer.COMMA]
        if seq[1] == vbaLexer.WS:
            if (
                    seq[0] in pre_single_ws or
                    len(seq) > 2 and seq[2] in post_single_ws
               ):
                output.append((1, 1, "1"))
            token = ts.LT(2)
            assert isinstance(token, Token)
            text = token.text.replace("\t", " " * 8)
            pre_exceptions = [vbaLexer.NEWLINE, vbaLexer.LINE_CONTINUATION,
                              vbaLexer.COLON]
            post_exceptions = [vbaLexer.AS, vbaLexer.COMMENT]
            # Arbitrary whitespace is allowed at the beginning
            # of lines, after a colon, before comments, and before
            # an As statement. The 'As' exception is only valid in
            # a Dim or const statement.
            if (
                    len(text) > 1 and
                    seq[0] not in pre_exceptions and
                    (
                        len(seq) < 3 or
                        seq[2] not in post_exceptions
                    )
            ):
                line = token.line
                column = token.column
                rule = "001"
                output.append((line, column, rule))
        return output

    def _build_list(self: T, ts: CommonTokenStream, num: int) -> list:
        """
        extract the next specified number of tokens from the stream.
        """
        found_eof = False
        token_types: List[int] = []
        for i in range(num):
            if found_eof:
                return token_types
            tok_type = ts.LA(i + 1)
            if tok_type == Token.EOF:
                found_eof = True
            token_types.append(tok_type)
        return token_types
