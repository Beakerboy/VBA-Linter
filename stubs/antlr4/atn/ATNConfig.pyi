from _typeshed import Incomplete
from antlr4.PredictionContext import PredictionContext as PredictionContext
from antlr4.atn.ATNState import ATNState as ATNState, DecisionState as DecisionState
from antlr4.atn.LexerActionExecutor import LexerActionExecutor as LexerActionExecutor
from antlr4.atn.SemanticContext import SemanticContext as SemanticContext

class ATNConfig:
    state: Incomplete
    alt: Incomplete
    context: Incomplete
    semanticContext: Incomplete
    reachesIntoOuterContext: Incomplete
    precedenceFilterSuppressed: Incomplete
    def __init__(self, state: ATNState = ..., alt: int = ..., context: PredictionContext = ..., semantic: SemanticContext = ..., config: ATNConfig = ...) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def hashCodeForConfigSet(self): ...
    def equalsForConfigSet(self, other): ...

class LexerATNConfig(ATNConfig):
    lexerActionExecutor: Incomplete
    passedThroughNonGreedyDecision: Incomplete
    def __init__(self, state: ATNState, alt: int = ..., context: PredictionContext = ..., semantic: SemanticContext = ..., lexerActionExecutor: LexerActionExecutor = ..., config: LexerATNConfig = ...) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def hashCodeForConfigSet(self): ...
    def equalsForConfigSet(self, other): ...
    def checkNonGreedyDecision(self, source: LexerATNConfig, target: ATNState): ...
