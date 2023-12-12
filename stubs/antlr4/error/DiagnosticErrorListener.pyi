from _typeshed import Incomplete
from antlr4 import Parser as Parser, DFA as DFA
from antlr4.atn.ATNConfigSet import ATNConfigSet as ATNConfigSet
from antlr4.error.ErrorListener import ErrorListener as ErrorListener

class DiagnosticErrorListener(ErrorListener):
    exactOnly: Incomplete
    def __init__(self, exactOnly: bool = ...) -> None: ...
    def reportAmbiguity(self, recognizer: Parser, dfa: DFA, startIndex: int, stopIndex: int, exact: bool, ambigAlts: set, configs: ATNConfigSet): ...
    def reportAttemptingFullContext(self, recognizer: Parser, dfa: DFA, startIndex: int, stopIndex: int, conflictingAlts: set, configs: ATNConfigSet): ...
    def reportContextSensitivity(self, recognizer: Parser, dfa: DFA, startIndex: int, stopIndex: int, prediction: int, configs: ATNConfigSet): ...
    def getDecisionDescription(self, recognizer: Parser, dfa: DFA): ...
    def getConflictingAlts(self, reportedAlts: set, configs: ATNConfigSet): ...
