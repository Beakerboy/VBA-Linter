import sys
from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser

class CalcListener(ParseTreeListener):
    def exitExpr(self, ctx: CalcParser.ExprContext):
        if ctx.op is not None:
            ctx.value = int(ctx.expr(0).value) + int(ctx.expr(1).value) if ctx.op.text == '+' else int(ctx.expr(0).value) - int(ctx.expr(1).value)
        else:
            ctx.value = int(ctx.INT().getText())

def main(argv):
    input_stream = InputStream(argv[1])
    lexer = CalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcParser(stream)
    tree = parser.expr()

    listener = CalcListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(tree.value)

if __name__ == '__main__':
    main(sys.argv)
