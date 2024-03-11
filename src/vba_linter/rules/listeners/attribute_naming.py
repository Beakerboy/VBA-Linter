from antlr4 import ParseTreeListener, ParserRuleContext
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
import vba_linter.helpers.string_format
from vba_linter.rules.listeners.vba_listener_rule_base import VbaListenerRuleBase


T = TypeVar('T', bound='AttributeNaming')


class AttributeNaming(VbaListenerRuleBase):
    """
    Check that each atteibute is named correctly.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def enterLetStatement(self: T,  # noqa: N802
                          ctx: vbaParser.LetStatementContext) -> None:
        """
        foo = 7
        Let bar = True
        """
        tokens = VbaListener.get_tokens(ctx)
        tok = tokens[0] if tokens[0].type == vbaLexer.IDENTIFIER else tokens[2]
        if not VbaListener.is_snake_case(tok.text):
            msg = "variable not snake"
            output = (tok.line, tok.column + 2, "Wxxx", msg)
            self.output.append(output)

    def enterVariableDcl(self: T,  # noqa: N802
                         ctx: vbaParser.VariableDclContext) -> None:
        """
        Dim foo as Integer
        Dim a, b, c As Single, x, y As Double, i As Integer
        """
        tokens = VbaListener.get_tokens(ctx)
        for tok in tokens:
            if (tok.type == vbaLexer.IDENTIFIER and not
                    string_format.is_snake_case(tok.text)):
                msg = "variable not snake"
                output = (tok.line, tok.column + 2, "Wxxx", msg)
                self.output.append(output)

    def enterFunctionName(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionNameContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubroutineName(self: T,  # noqa: N802
                            ctx: vbaParser.SubroutineNameContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        tokens = VbaListener.get_tokens(ctx)
        token = tokens[2]
        if tokens[2].type == vbaLexer.IDENTIFIER:
            token = tokens[2]
        else:
            assert tokens[4].type == vbaLexer.IDENTIFIER
            token = tokens[4]
        if not string_format.is_pascal_case(token.text):
            line = token.line
            column = token.column
            msg = "name not Pascal"
            self.output.append((line, column + 2, "Wxxx", msg))
