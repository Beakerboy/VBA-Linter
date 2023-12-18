from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        ex.msg = msg
        raise ex
