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
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if 'prev_tok' in locals() and prev_tok.type == vbaLexer.WS:
                    output.append((line_num, "W200"))
                num = len(token.text)
                i = 0
                while i < num:
                    if num >= 2 and token.text[i:i+2] == '\r\n':
                        line_num += 1
                        i += 2
                    else:
                        output.append((line_num, "W400"))
                        line_num += 1
                        i += 1
            prev_tok = token
        output.sort()
        return output
