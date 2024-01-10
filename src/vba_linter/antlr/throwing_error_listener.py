from antlr4.error.ErrorListener import ErrorListener
from vba_linter.antlr.thrown_exception import ThrownException
from typing import Any, TypeVar


T = TypeVar('T', bound='ThrowingErrorListener')


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self: T, recognizer,  # noqa: N802
                    offending_symbol: Any, line: int,
                    column: int, msg: str, e: Exception) -> None:
        ex = ThrownException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        ex.msg = msg
        raise ex
