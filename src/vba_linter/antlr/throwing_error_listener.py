from antlr4.error.ErrorListener import ErrorListener
from antlr.thrown_exception import ThrownException

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ThrownException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        ex.msg = msg
        raise ex
