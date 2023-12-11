import sys
from antlr4 import CommonTokenStream, InputStream
import VBALexer
import VBAParser

def main(argv):
    input_stream = InputStream(argv[1])
    lexer = CalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    tokens = stream.getTokens()
    for token in tokens:
        if token.type == VBALexer.WS:
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
