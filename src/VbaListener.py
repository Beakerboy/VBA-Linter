from antlr import *

class VbaListener(ParseTreeListener):

    def exitExpr(self, ctx: CalcParser.ExprContext):
        if ctx.op is not None:
            ctx.value = int(ctx.expr(0).value) + int(ctx.expr(1).value) if ctx.op.text == '+' else int(ctx.expr(0).value) - int(ctx.expr(1).value)
        else:
            ctx.value = int(ctx.INT().getText())
