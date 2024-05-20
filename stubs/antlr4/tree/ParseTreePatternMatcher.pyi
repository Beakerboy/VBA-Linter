from _typeshed import Incomplete
from antlr4.CommonTokenStream import CommonTokenStream as CommonTokenStream
from antlr4.InputStream import InputStream as InputStream
from antlr4.Lexer import Lexer as Lexer
from antlr4.ListTokenSource import ListTokenSource as ListTokenSource
from antlr4.ParserRuleContext import ParserRuleContext as ParserRuleContext
from antlr4.Token import Token as Token
from antlr4.error.ErrorStrategy import BailErrorStrategy as BailErrorStrategy
from antlr4.error.Errors import ParseCancellationException as ParseCancellationException, RecognitionException as RecognitionException
from antlr4.tree.Chunk import TagChunk as TagChunk, TextChunk as TextChunk
from antlr4.tree.RuleTagToken import RuleTagToken as RuleTagToken
from antlr4.tree.TokenTagToken import TokenTagToken as TokenTagToken
from antlr4.tree.Tree import ParseTree as ParseTree, RuleNode as RuleNode, TerminalNode as TerminalNode

Parser: Incomplete
ParseTreePattern: Incomplete

class CannotInvokeStartRule(Exception):
    def __init__(self, e: Exception) -> None: ...

class StartRuleDoesNotConsumeFullPattern(Exception): ...

class ParseTreePatternMatcher:
    lexer: Incomplete
    parser: Incomplete
    start: str
    stop: str
    escape: str
    def __init__(self, lexer: Lexer, parser: Parser) -> None: ...
    def setDelimiters(self, start: str, stop: str, escapeLeft: str): ...
    def matchesRuleIndex(self, tree: ParseTree, pattern: str, patternRuleIndex: int): ...
    def matchesPattern(self, tree: ParseTree, pattern: ParseTreePattern): ...
    def matchRuleIndex(self, tree: ParseTree, pattern: str, patternRuleIndex: int): ...
    def matchPattern(self, tree: ParseTree, pattern: ParseTreePattern): ...
    def compileTreePattern(self, pattern: str, patternRuleIndex: int): ...
    def matchImpl(self, tree: ParseTree, patternTree: ParseTree, labels: dict): ...
    def map(self, labels, label, tree) -> None: ...
    def getRuleTagToken(self, tree: ParseTree): ...
    def tokenize(self, pattern: str): ...
    def split(self, pattern: str): ...