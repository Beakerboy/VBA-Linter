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
        if token.type == vbaLexer.WS:
            cr = False
            lf = False
            if "\n" in token.text:
                lf = True
            if "\r" in token.text:
                cr = True
            if cr and lf:
                if token.text.index("\r") + 1 != token.text.index("\n"):
                    return "line: " + "incorrect line ending"
            if cr != lf:
                return "line: " + "incorrect line ending"
        output += str((token.text, token.type))
        return output

if __name__ == '__main__':
    main(sys.argv)
