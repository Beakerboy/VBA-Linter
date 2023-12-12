from _typeshed import Incomplete
from antlr4.Recognizer import Recognizer as Recognizer
from antlr4.RuleContext import RuleContext as RuleContext

class SemanticContext:
    NONE: Incomplete
    def eval(self, parser: Recognizer, outerContext: RuleContext): ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext): ...

AND: Incomplete

def andContext(a: SemanticContext, b: SemanticContext): ...

OR: Incomplete

def orContext(a: SemanticContext, b: SemanticContext): ...
def filterPrecedencePredicates(collection: set): ...

class EmptySemanticContext(SemanticContext): ...

class Predicate(SemanticContext):
    ruleIndex: Incomplete
    predIndex: Incomplete
    isCtxDependent: Incomplete
    def __init__(self, ruleIndex: int = ..., predIndex: int = ..., isCtxDependent: bool = ...) -> None: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class PrecedencePredicate(SemanticContext):
    precedence: Incomplete
    def __init__(self, precedence: int = ...) -> None: ...
    def eval(self, parser: Recognizer, outerContext: RuleContext): ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext): ...
    def __lt__(self, other): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class AND(SemanticContext):
    opnds: Incomplete
    def __init__(self, a: SemanticContext, b: SemanticContext) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def eval(self, parser: Recognizer, outerContext: RuleContext): ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext): ...

class OR(SemanticContext):
    opnds: Incomplete
    def __init__(self, a: SemanticContext, b: SemanticContext) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    def eval(self, parser: Recognizer, outerContext: RuleContext): ...
    def evalPrecedence(self, parser: Recognizer, outerContext: RuleContext): ...
