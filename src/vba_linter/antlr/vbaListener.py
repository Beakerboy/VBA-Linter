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
        self.ts: CommonTokenStream
        self.listeners: list = []

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def add_listener(self: T, listener: ParseTreeListener) -> None:
        self.listeners.append(listener)

    def enterEveryRule(self: T, ctx: ParserRuleContext) -> None:
        for listener in listeners:
            listener.enterEveryRule(ctx)
            ctx.enterRule(listener)

    def exitEveryRule(self: T, ctx: ParserRuleContext) -> None:
        for listener in listeners:
            ctx.exitRule(listener)
            listener.exitEveryRule(ctx)

    def visitErrorNode(self: T, node: ErrorNode) -> None:
        for listener in listeners:
            listener.visitErrorNode(node)

    def visitTerminal(self: T, node: TerminalNode) -> None:
        for listener in listeners:
            listener.visitTerminal(node)

    def enterLetStmt(self: T,  # noqa: N802
                     ctx: vbaParser.LetStmtContext) -> None:
        tokens = VbaListener.get_tokens(ctx)
        terminal_num = 0
        for tok in tokens:
            terminal_num += 1
            if terminal_num == 1 and tok.type != vbaLexer.LET:
                output = (tok.line, tok.column + 2, "Wxxx", "missing let")
                self.output.append(output)
            if tok.type == vbaLexer.LET:
                output = (tok.line, tok.column + 2, "Wxxx", "optional let")
                self.output.append(output)
            elif tok.type == vbaLexer.EQ:
                target = tok
                leading_index = target.tokenIndex - 1
                trailing_index = target.tokenIndex + 1
                tok = self.ts.get(leading_index)
                if tok.type == vbaLexer.WS:
                    if len(tok.text) > 1:
                        output1 = (tok.line, tok.column + 2, "W221")
                        self.output.append(output1)
                else:
                    output1 = (target.line, target.column + 1, "R225")
                    self.output.append(output1)
                tok = self.ts.get(trailing_index)
                if tok.type == vbaLexer.WS:
                    if len(tok.text) > 1:
                        output1 = (tok.line, tok.column + 2, "W221")
                        self.output.append(output1)
                else:
                    output1 = (target.line, target.column + 1, "R225")
                    self.output.append(output1)

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
        child = ctx.getChild(0)
        tokens = VbaListener.get_tokens(child)
        tok = tokens[0]
        if isinstance(child, vbaParser.VisibilityContext):
            if tok.text == "Public":
                self.output.append((tok.line, tok.column + 1,
                                    "Wxxx", "optional public"))
        else:
            line = tok.line
            column = token.column
            msg = "missing visibility"
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
