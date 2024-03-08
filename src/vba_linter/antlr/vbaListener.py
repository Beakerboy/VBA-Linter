from antlr4 import (CommonTokenStream, ErrorNode, ParseTreeListener,
                    ParserRuleContext, TerminalNode)
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4_vba.vbaParser import vbaParser
from typing import Type, TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='VbaListener')


class VbaListener(ParseTreeListener, RuleBase):
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []
        self.ts: CommonTokenStream
        self.listeners: list = []

    def set_token_stream(self: T, ts: CommonTokenStream) -> None:
        self.ts = ts

    def add_listener(self: T, listener: ParseTreeListener) -> None:
        self.listeners.append(listener)

    def get_output(self: T) -> list:
        for listener in self.listeners:
            self.output.extend(listener.output)
        return self.output

    def enterEveryRule(self: T, ctx: ParserRuleContext) -> None:  # noqa: 
        for listener in self.listeners:
            listener.enterEveryRule(ctx)
            ctx.enterRule(listener)

    def exitEveryRule(self: T, ctx: ParserRuleContext) -> None:  # noqa: 
        for listener in self.listeners:
            ctx.exitRule(listener)
            listener.exitEveryRule(ctx)

    def enterStartRule(  # noqa: N802
            self: T,
            ctx: vbaParser.StartRuleContext) -> None:
        self.output = []

    def visitErrorNode(self: T, node: ErrorNode) -> None:  # noqa: 
        for listener in self.listeners:
            listener.visitErrorNode(node)

    def visitTerminal(self: T, node: TerminalNode) -> None:  # noqa: 
        for listener in self.listeners:
            listener.visitTerminal(node)

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
        """
        Follow the parse tree down to capture all the tokens within
        this context, essentially building a truncated tokenstream.
        """
        tokens = []
        if isinstance(ctx, TerminalNodeImpl):
            return [ctx.getSymbol()]
        else:
            for child in ctx.getChildren():
                tokens.extend(cls.get_tokens(child))
        return tokens
