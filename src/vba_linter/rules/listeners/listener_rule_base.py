from antlr4 import ParserRuleContext, ParseTreeListener
from antlr4.tree.Tree import TerminalNodeImpl
from typing import Type, TypeVar
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='ListenerRuleBase')


class ListenerRuleBase(ParseTreeListener, RuleBase):
    """
    A common interface for ListenerRules.
    """
    def __init__(self: T) -> None:
        super().__init__()
        self.output: list = []

    @classmethod
    def get_tokens(cls: Type[T], ctx: ParserRuleContext) -> list:
        """
        Follow the parse tree down to capture all the tokens within
        this context, essentially building a truncated tokenstream.
        """
        tokens = []
        if isinstance(ctx, TerminalNodeImpl):
            return [ctx.symbol]
        else:
            for child in ctx.getChildren():
                tokens.extend(cls.get_tokens(child))
        return tokens
