from antlr4 import CommonTokenStream, ParseTreeWalker
from vba_linter.rules.listeners.missing_let import MissingLet

listener = MissingLet()
listener.set_token_stream(ts1)
ParseTreeWalker.DEFAULT.walk(rule, program)
listener.get_output()
