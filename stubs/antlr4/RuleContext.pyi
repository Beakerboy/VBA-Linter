from _typeshed import Incomplete
from antlr4.tree.Tree import INVALID_INTERVAL as INVALID_INTERVAL, ParseTreeVisitor as ParseTreeVisitor, RuleNode as RuleNode
from antlr4.tree.Trees import Trees as Trees
from collections.abc import Generator

RuleContext: Incomplete
Parser: Incomplete

class RuleContext(RuleNode):
    EMPTY: Incomplete
    parentCtx: Incomplete
    invokingState: Incomplete
    def __init__(self, parent: RuleContext = ..., invokingState: int = ...) -> None: ...
    def depth(self): ...
    def isEmpty(self): ...
    def getSourceInterval(self): ...
    def getRuleContext(self): ...
    def getPayload(self): ...
    def getText(self): ...
    def getRuleIndex(self): ...
    def getAltNumber(self): ...
    def setAltNumber(self, altNumber: int): ...
    def getChild(self, i: int): ...
    def getChildCount(self): ...
    def getChildren(self) -> Generator[Incomplete, None, None]: ...
    def accept(self, visitor: ParseTreeVisitor): ...
    def toStringTree(self, ruleNames: list = ..., recog: Parser = ...): ...
    def toString(self, ruleNames: list, stop: RuleContext) -> str: ...
