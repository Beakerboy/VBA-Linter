import sys
from antlr4 import CommonTokenStream, InputStream
from vbaLexer import vbaLexer

def main(argv):
    input_stream = InputStream(argv[1])
    lexer = vbaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    tokens = stream.getAllTokens()
    for token in tokens:
        if token.type == vbaLexer.WS:
            cr = False
            lf = False
            if "\n" in token.text:
                lf = True
            if "\r" in token.text:
                cr = True
            if cr and lf:
                if token.text.index("\r") + 1 != token.text.index("\n"):
                    print("line: " + "incorrect line ending")
            if cr != lf:
                print("line: " + "incorrect line ending")

if __name__ == '__main__':
    main(sys.argv)
