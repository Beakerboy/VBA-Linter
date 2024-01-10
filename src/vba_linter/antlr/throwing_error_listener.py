from antlr4.error.ErrorListener import ErrorListener
from vba_linter.antlr.thrown_exception import ThrownException
from typing import TypeVar


T = TypeVar('T', bound='ThrowingErrorListener')


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self: T, recognizer, offending_symbol, line: int,
                    column: int, msg: str, e):
        ex = ThrownException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        ex.msg = msg
        raise ex
