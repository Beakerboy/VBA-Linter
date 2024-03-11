from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser as Parser
from typing import Dict, List, TypeVar
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase



T = TypeVar('T', bound='ExcessWhitespace')


class ExcessWhitespace(ListenerRuleBase):

    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._rule_name = "151"
        self._message = "Excess whitespace {3} '{4}'"
        self.rules: Dict[str, int] = {'(': 121, ')': 131, ',': 141,
                                      '=': 151, ':=': 161, ':': 191}
        self._fixable = True

    def test(self: T, ts: CommonTokenStream) -> list:
        symbols = ['=', ':=', ':', ',']
        output: List[tuple] = []
        seq = self._build_list(ts, 3)
        # Tokens which must have no whitespace after.
        pre_single_ws = [vbaLexer.ASSIGN, vbaLexer.LPAREN]
        # Tokens which must have no whitespace before.
        post_single_ws = [vbaLexer.COLON, vbaLexer.ASSIGN,
                          vbaLexer.COMMA, vbaLexer.RPAREN]
        post_single_ws_exception = {vbaLexer.COMMA: [vbaLexer.COMMA]}
        if seq[1] == vbaLexer.WS:
            token = ts.LT(2)
            assert isinstance(token, Token)
            line = token.line
            column = token.column + 1
            text = token.text.replace("\t", " " * 8)
            pre_exceptions = [vbaLexer.NEWLINE, vbaLexer.LINE_CONTINUATION,
                              vbaLexer.COLON]
            post_exceptions = [vbaLexer.AS, vbaLexer.COMMENT]
            # check the cases where even the existence of whitespace is an
            # error.
            if seq[0] in pre_single_ws:
                pre_token = ts.LT(1)
                assert isinstance(pre_token, Token)
                text = pre_token.text
                rule = self._rule_name + ':' + str(self.rules[text] + 3)
                output.append((line, column, rule, "after", text))
            elif (
                    len(seq) > 2 and seq[2] in post_single_ws and
                    (seq[2] != vbaLexer.COLON or seq[0] != vbaLexer.COLON)
                 ):
                if (
                    seq[2] not in post_single_ws_exception or
                    seq[0] not in post_single_ws_exception[seq[2]]
                ):
                    post_token = ts.LT(3)
                    assert isinstance(post_token, Token)
                    text = post_token.text
                    rule = self._rule_name + ':' + str(self.rules[text])
                    otp = (line, column, rule, "before", text)
                    if rule == "151:141":
                        self.output.append(otp)
                    else:
                        output.append(otp)
            # Arbitrary whitespace is allowed at the beginning
            # of lines, after a colon, before comments, and before
            # an As statement. The 'As' exception is only valid in
            # a Dim or const statement.
            elif (
                    len(text) > 1 and
                    seq[0] not in pre_exceptions and
                    (
                        len(seq) < 3 or
                        seq[2] not in post_exceptions
                    )
            ):
                line = token.line
                column = token.column + 2
                symbol = ""
                pre_token = ts.LT(1)
                assert isinstance(pre_token, Token)
                where = ""
                if pre_token.text in symbols:
                    symbol = pre_token.text
                    rule = self._rule_name + ':' + str(self.rules[symbol] + 3)
                    where = 'after'
                elif len(seq) > 2:
                    post_token = ts.LT(3)
                    assert isinstance(post_token, Token)
                    if post_token.text in symbols:
                        symbol = post_token.text
                        rule = self._rule_name + ':' + str(self.rules[symbol])
                        where = 'before'
                if symbol == "":
                    symbol = "identifier"
                output.append((line, column, rule, where, symbol))
        return output

    def create_message(self: T, data: tuple) -> str:
        data_list = list(data)
        message = "Excess whitespace {3} '{4}'"
        rules: Dict[str, int] = {'(': 121, ')': 131, ',': 141, '=': 151}
        if data[4] in rules:
            data_list[2] = data_list[2][-3:]
        msg_str = ":{0}:{1}: " + self._severity + "{2} " + message
        return msg_str.format(*data_list)

    def enterArgumentList(self: T,  # noqa: N802
                          ctx: Parser.ArgumentListContext) -> None:
        """
        There is a rare case of omitting the first argument in a subroutine
        call:
        MiscSub , Arg  ' This is fine
        Call MiscSub( , Arg)  ' This is Not
        Call MiscSub(, Arg)  ' This is Fine
        The whitespace after the subroutine name is manditory, so there must be
        whitespace before a comma.
        """
        exit()
        tokens = ListenerRuleBase.get_tokens(ctx)
        raise Exception(str(tokens[0]))
        if tokens[1].type == vbaLexer.COMMA:
            raise Exception(str(tokens[0]))
            parent = ctx.parentCtx
            if isinstance(parent, Parser.CallStatementContext):
                ws = parent.getChild(0, Parser.WscContext)
                wsc = ws.getChild(0).symbol
                raise Exception(str(wsc))
                for item in self.output:
                    if item == (wsc.line, wsc.column + 1,
                                "151:141", 'before', ','):
                        self.output.remove(item)

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
