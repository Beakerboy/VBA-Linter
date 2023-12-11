import sys
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer


def main(argv: list) -> str:
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
            else:
                output += str(token.type)
            if prev_tok == vbaLexer.WS:
                output += "line: " + str(line_num)
                output += " whitespace at the end of the line.\n"
            line_num += 1
            prev_tok = token
    return output


if __name__ == '__main__':
    main(sys.argv)
