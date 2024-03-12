from antlr4 import ParserRuleContext
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='ArglistWs')


class ArglistWs(ListenerRuleBase):
    """
    Inspect the whitespace before an argument list to
    ensure there is no whitespace between the function
    name and the left parenthesis.
    We need to use a listener in order to differentiate
    between the following cases:
    MiscSub (1 + 2)  ' Fine: parenthesised expression as arg
    Call MiscSub (1 + 2)  'Bad: space between name and arglist
    Foo = MiscFunc (1 + 2)  ' Bad: space between name and arglist
    Whitespace is expected between a stringliteral and arglist
    in declare statements.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self.rule_name = "121"
        self.msg = "Excess whitespace before '('"

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
            paren_index = parens[0].symbol.tokenIndex

            def predicate(x: object) -> bool:
                return isinstance(x, vbaParser.WscContext)

            spaces = ctx.getChildren(predicate)
            for wsc in spaces:
                if wsc.getChild(0).symbol.tokenIndex == paren_index - 1:
                    ws = wsc.getChild(0).symbol
                    msg = self.msg
                    line = ws.line
                    column = ws.column + 1
                    rule = self.rule_name
                    self.output.append((line, column, rule, msg))

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
        if not isinstance(vbaParser.ExternalFunctionContext, parent)
            paren_index = token.tokenIndex

            def predicate(x: object) -> bool:
                return isinstance(x, vbaParser.WscContext)

            spaces = parent.getChildren(predicate)
            for wsc in spaces:
                if wsc.getChild(0).symbol.tokenIndex == paren_index - 1:
                    ws = wsc.getChild(0).symbol
                    msg = self.msg
                    line = ws.line
                    column = ws.column + 1
                    rule = self.rule_name
                    self.output.append((line, column, rule, msg))
                    break
