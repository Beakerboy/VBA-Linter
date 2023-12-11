import sys
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer


def main(argv: list) -> str:
    input_stream = InputStream(argv[1])
    lexer = vbaLexer(input_stream)
    tokens = lexer.getAllTokens()
    for token in tokens:
        if token.type == vbaLexer.NEWLINE:
            if token.text == "\n":
                return "line: " + "incorrect line ending"


if __name__ == '__main__':
    main(sys.argv)
