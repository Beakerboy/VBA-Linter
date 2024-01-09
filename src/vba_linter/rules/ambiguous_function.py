from antlr4 import Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.rules.ambiguous_identifier import AmbiguousIdentifier
from typing import TypeVar


T = TypeVar('T', bound='AmbiguousFunction')


class AmbiguousFunction(AmbiguousIdentifier):
    def __init__(self: T) -> None:
        self._rule_name = "E743"
        self._names = ['l', 'O', 'I']
        self._message = 'ambiguous function name'
        self._sequence = [vbaLexer.FUNCTION, vbaLexer.WS, vbaLexer.IDENTIFIER]
        self._target = 3
