import sys
from antlr4 import InputStream
from vba_linter.vbaLexer import vbaLexer


def main(argv: list) -> str:
    input_stream = InputStream(argv[1])
    lexer = vbaLexer(input_stream)
    #stream = CommonTokenStream(lexer)
    tokens = lexer.getAllTokens()
    for token in tokens:
        output = ""
        if token.type == vbaLexer.NEWLINE:
            if token.text == "\n":
                return "line: " + "incorrect line ending"
        output += str((token.text, token.type))
    return output

if __name__ == '__main__':
    main(sys.argv)
