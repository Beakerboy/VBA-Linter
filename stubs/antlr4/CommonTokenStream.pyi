from _typeshed import Incomplete
from antlr4.BufferedTokenStream import BufferedTokenStream as BufferedTokenStream
from antlr4.Lexer import Lexer as Lexer
from antlr4.Token import Token as Token

class CommonTokenStream(BufferedTokenStream):
    channel: Incomplete
    def __init__(self, lexer: Lexer, channel: int = ...) -> None: ...
    def adjustSeekIndex(self, i: int): ...
    def LB(self, k: int): ...
    def LT(self, k: int): ...
    def getNumberOfOnChannelTokens(self): ...
