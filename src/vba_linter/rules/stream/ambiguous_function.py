from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.stream.ambiguous_identifier import AmbiguousIdentifier
from typing import TypeVar


T = TypeVar('T', bound='AmbiguousFunction')


class AmbiguousFunction(AmbiguousIdentifier):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "743"
        self._message = 'ambiguous function name'
        self._sequence = [vbaLexer.FUNCTION, vbaLexer.WS, vbaLexer.IDENTIFIER]
        self._target = 3
