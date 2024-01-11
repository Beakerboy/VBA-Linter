import re
from antlr4 import CommonTokenStream, ParseTreeListener, ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4_vba.vbaLexer import vbaLexer
from antlr4_vba.vbaParser import vbaParser
from typing import Type, TypeVar


T = TypeVar('T', bound='VbaListener')


class VbaListener(ParseTreeListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def enterLetStmt(self: T,  # noqa: N802
                     ctx: vbaParser.LetStmtContext) -> None:
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

    def enterVariableStmt(self: T,  # noqa: N802
                          ctx: vbaParser.VariableStmtContext) -> None:
        """
        Dim foo as Integer
        Dim a, b, c As Single, x, y As Double, i As Integer
        """
        tokens = VbaListener.get_tokens(ctx)
        for tok in tokens:
            if (tok.type == vbaLexer.IDENTIFIER and not
                    VbaListener.is_snake_case(tok.text)):
                msg = "variable not snake"
                output = (tok.line, tok.column + 2, "Wxxx", msg)
                self.output.append(output)

    def enterFunctionStmt(self: T,  # noqa: N802
                          ctx: vbaParser.FunctionStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enterSubStmt(self: T,  # noqa: N802
                     ctx: vbaParser.SubStmtContext) -> None:
        self.enter_function_sub_stmt(ctx)

    def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        tokens = VbaListener.get_tokens(ctx)
        token = tokens[2]
        if tokens[2].type == vbaLexer.IDENTIFIER:
            token = tokens[2]
        else:
            assert tokens[4].type == vbaLexer.IDENTIFIER
            token = tokens[4]
        if not VbaListener.is_pascal_case(token.text):
            line = token.line
            column = token.column
            msg = "name not Pascal"
            self.output.append((line, column + 2, "Wxxx", msg))

    @classmethod
    def text_matches(cls: Type[T], pattern: str, name: str) -> bool:
        match = re.match(pattern, name)
        if match:
            return True
        return False

    @classmethod
    def is_snake_case(cls: Type[T], name: str) -> bool:
        pattern = '(^[a-z]{1}$)|([a-z]+(_[a-z]+)*$)'
        return cls.text_matches(pattern, name)

    @classmethod
    def is_camel_case(cls: Type[T], name: str) -> bool:
        """
        Also known as lowerCamelCase.
        """
        pattern = '(^[a-z]{1}$)|([a-z]{2,}([a-zA-Z]([a-z])+)*$)'
        return cls.text_matches(pattern, name)

    @classmethod
    def is_pascal_case(cls: Type[T], name: str) -> bool:
        """
        Also known as UpperCamelCase.
        """
        pattern = '(^[a-z]{1}$)|(([A-Z]([a-z])+)*$)'
        return cls.text_matches(pattern, name)

    @classmethod
    def get_tokens(cls: Type[T], ctx: ParserRuleContext) -> list:
        tokens = []
        if isinstance(ctx, TerminalNodeImpl):
            return [ctx.getSymbol()]
        else:
            for child in ctx.getChildren():
                tokens.extend(cls.get_tokens(child))
        return tokens