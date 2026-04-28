from antlr4 import CommonTokenStream, ParserRuleContext
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import TypeVar
from vba_linter.helpers.string_format import is_pascal_case
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='FunctionNaming')


class FunctionNaming(ListenerRuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self._message = "name not Pascal"

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterFunctionName(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionNameContext) -> None:
        self.enter_function_sub_name(ctx)

    def enterSubroutineName(  # noqa: N802
            self: T,
            ctx: vbaParser.SubroutineNameContext
    ) -> None:
        self.enter_function_sub_name(ctx)

    def enter_function_sub_name(self: T, ctx: ParserRuleContext) -> None:
        token = ctx.start
        if (
                token.type == vbaLexer.IDENTIFIER and
                not is_pascal_case(token.text)
        ):
            line = token.line
            column = token.column
            self.output.append((line, column + 2, "Wxxx"))
