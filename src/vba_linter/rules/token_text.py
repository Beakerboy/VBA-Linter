from antlr4 import CommonTokenStream, Token
from antlr4_vba.vbaLexer import vbaLexer as Lexer
from vba_linter.rules.rule_base import RuleBase
from typing import TypeVar


T = TypeVar('T', bound='TokenText')


class TokenText(RuleBase):
    """
    report if the text of a token does not match the target.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.rule_name = '183'
        self._message = "Incorrect symbol format"

    def test(self: T, ts: CommonTokenStream) -> list:
        output = []
        targets = {
            Lexer.GT: ">=", Lexer.LT: "<=", Lexer.NEQ: "<>",
        }
        tok = ts.LT(1)
        assert isinstance(tok, Token)
        if tok.type in targets and tok.text != targets[tok.type]:
            line = tok.line
            col = tok.column + 1
            rule = self.rule_name
            output.append((line, col, rule))
        return output
