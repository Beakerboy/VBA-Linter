from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer
from typing import TypeVar

T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        pass

    def lint(self: T, code: str) -> list:
        input_stream = InputStream(code)
        lexer = vbaLexer(input_stream)
        tokens = lexer.getAllTokens()
        line_num = 1
        output = []
        prev_tok: antlr4.Token = None
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if token.text == "\n" or token.text == "\r":
                    output.append((line_num, "W400"))
                if not (prev_tok is None) and prev_tok.type == vbaLexer.WS:
                    output.append((line_num, "W200"))
                line_num += 1
            prev_tok = token
        output.sort()
        return output
