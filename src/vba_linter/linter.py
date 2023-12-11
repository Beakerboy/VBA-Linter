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
        input_stream = InputStream(argv[1])
        lexer = vbaLexer(input_stream)
        tokens = lexer.getAllTokens()
        line_num = 1
        output = ""
        prev_tok = ""
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if token.text == "\n":
                    output += "line: " + str(line_num) + " incorrect line ending\n"
                if prev_tok != "" and prev_tok.type == vbaLexer.WS:
                    output += "line: " + str(line_num)
                    output += " trailing whitespace\n"
                line_num += 1
            prev_tok = token
        return output
