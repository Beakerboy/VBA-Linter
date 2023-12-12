from _typeshed import Incomplete
from antlr4.RuleContext import RuleContext as RuleContext
from antlr4.Token import Token as Token
from antlr4.error.ErrorListener import ConsoleErrorListener as ConsoleErrorListener, ProxyErrorListener as ProxyErrorListener

RecognitionException: Incomplete

class Recognizer:
    tokenTypeMapCache: Incomplete
    ruleIndexMapCache: Incomplete
    def __init__(self) -> None: ...
    def extractVersion(self, version): ...
    def checkVersion(self, toolVersion) -> None: ...
    def addErrorListener(self, listener) -> None: ...
    def removeErrorListener(self, listener) -> None: ...
    def removeErrorListeners(self) -> None: ...
    def getTokenTypeMap(self): ...
    def getRuleIndexMap(self): ...
    def getTokenType(self, tokenName: str): ...
    def getErrorHeader(self, e: RecognitionException): ...
    def getTokenErrorDisplay(self, t: Token): ...
    def getErrorListenerDispatch(self): ...
    def sempred(self, localctx: RuleContext, ruleIndex: int, actionIndex: int): ...
    def precpred(self, localctx: RuleContext, precedence: int): ...
    @property
    def state(self): ...
    @state.setter
    def state(self, atnState: int): ...
