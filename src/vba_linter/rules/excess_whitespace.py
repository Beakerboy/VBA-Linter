from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from typing import Dict, List, TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='ExcessWhitespace')


class ExcessWhitespace(RuleBase):

    def test(self: T, ts: CommonTokenStream) -> list:
        symbols = ['=', ':=', ':', ',']
        output: List[tuple] = []
        seq = self._build_list(ts, 3)
        # Tokens which must have no whiteapace after.
        pre_single_ws = [vbaLexer.ASSIGN]
        # Tokens which must have no whitespace before.
        post_single_ws = [vbaLexer.COLON, vbaLexer.ASSIGN, vbaLexer.COMMA]
        if seq[1] == vbaLexer.WS:
            token = ts.LT(2)
            assert isinstance(token, Token)
            line = token.line
            column = token.column + 1
            # check the cases where even the existence of whitespace is an
            # error.
            if seq[0] in pre_single_ws:
                output.append((line, column, "001", "after", seq[0].text))
            elif (
                    len(seq) > 2 and seq[2] in post_single_ws and
                    (seq[2] != vbaLexer.COLON or seq[0] != vbaLexer.COLON)
                 ):
                post_token token = ts.LT(3)
                assert isinstance(post_token, Token)
                output.append((line, column, "001", "before", post_token.text))
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
                column = token.column + 2
                rule = "001"
                symbol = ""
                pre_token = ts.LT(1)
                assert isinstance(pre_token, Token)
                if pre_token.text in symbols:
                    symbol = pre_token.text
                elif len(seq) > 2:
                    post_token = ts.LT(3)
                    assert isinstance(post_token, Token)
                    if post_token.text in symbols:
                        symbol = post_token.text
                if symbol == "":
                    symbol = "identifier"
                output.append((line, column, rule, "after", symbol))
        return output

    def create_message(self: T, data: tuple) -> str:
        data_list = list(data)
        message = "Excess whitespace {3} '{4}'"
        rules: Dict[str, int] = {',': 140, '=': 150}
        if data[3] in rules:
            data_list[2] = str(rules[data[4]] + 1)
        msg_str = ":{0}:{1}: " + self._severity + "{2} " + message
        return msg_str.format(*data_list)

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
