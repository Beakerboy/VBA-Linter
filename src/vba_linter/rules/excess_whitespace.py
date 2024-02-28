class ExcessWhitespace(RuleBase):
    def test(self: T, ts: CommonTokenStream) -> list:
        seq = self._build_list(ts, 3)
        if seq[1] == vbaLexer.WS:
            token = ts.LT(i + 1)
            text = token.text.replace("\t", " " * 8)
            # Arbitrary whitespace is allowed at the beginning
            # of lines, after a colon, before comments, and before
            # an As statement. The 'As' exception is only valid in
            # a Dim or const statement.
            if (
                    len(text) > 1 and
                    seq[0] != vbaLexer.NEWLINE and
                    seq[0] != vbaLexer.LINE_CONTINUATION and
                    seq[3] != vbaLexer.AS and
                    seq[3] != vbaLexer.COMMENT
            )
            
    def _build_list(self: T, ts:CommonTokenStream, num: int) -> list:
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