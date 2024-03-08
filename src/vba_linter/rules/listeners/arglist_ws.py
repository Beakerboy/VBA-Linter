from antlr4 import ParserRuleContext, ParseTreeListener
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar


T = TypeVar('T', bound='ArglistWs')


class ArglistWs(ParseTreeListener):
    """
    Inspect the whitespace before an argument list to
    ensure there is no whitespace between the function
    name and the left parenthesis.
    We need to use a listener in order to differentiate
    between the following cases:
    MiscSub (1 + 2)  ' Fine: parenthesised expression as arg
    Call MiscSub (1 + 2)  'Bad: space between name and arglist
    Foo = MiscFunc (1 + 2)  ' Bad: space between name and arglist
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterLExpression(self: T,  # noqa: N802
                         ctx: vbaParser.LExpressionContext) -> None:
        self.test_expression(ctx)

    def enterIndexExpression(self: T,  # noqa: N802
                             ctx: vbaParser.IndexExpressionContext) -> None:
        """
        An argumentList may or may not have a parenthesis depending on
        if it is a sub or if it is a 'Call'ed sub, or a Let statement.
        """
        self.test_expression(ctx)

    def test_expression(self: T, ctx: ParserRuleContext) -> None:
        parens = ctx.getTokens(vbaLexer.LPAREN)
        if len(parens) > 0:
            paren_index = parens[0].tokenIndex
            spaces = ctx.getTokens(vbaLexer.WS)
            for ws in spaces:
                if ws.tokenIndex == paren_index - 1:
                    self.output.append((ws.line, ws.column, "221"))

    def enterProcedureParameters(self: T,  # noqa: N802
                                 ctx: vbaParser.ProcedureParametersContext
                                 ) -> None:
        self.check_parameters(ctx)

    def enterPropertyParameters(self: T,  # noqa: N802
                                ctx: vbaParser.PropertyParametersContext
                                ) -> None:
        self.check_parameters(ctx)

    def check_parameters(self: T, ctx: ParserRuleContext) -> None:
        """
        Check the parameter list for functions, subs, and properties.
        Best Practice:
        Function Foo(Bar)
        Anti-Pattern:
        Function Foo (Bar)
        """
        token = ctx.start
        parent = ctx.parentCtx
        paren_index = token.tokenIndex

        def predicate(x: object) -> bool:
            return isinstance(x, vbaParser.WscContext)

        spaces = parent.getChildren(predicate)
        for ws in spaces:
            if ws.symbol.tokenIndex == paren_index - 1:
                self.output.append((ws.line, ws.column, "221"))
                break
