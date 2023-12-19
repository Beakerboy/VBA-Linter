from antlr4.error.Errors import ParseCancellationException

class ThrownException(ParseCancellationException):

    def __init__(self, message):
        super().__init__(message)
        self.msg = ''
        self.line = 0
        self.column = 0
