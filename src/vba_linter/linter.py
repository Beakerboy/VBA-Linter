import re
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.antlr.throwing_error_listener import ThrowingErrorListener
from vba_linter.antlr.vbaListener import vbaListener
from pathlib import Path
from typing import Type, TypeVar
from vba_linter.rule_directory import RuleDirectory
from vba_linter.rules.parsing_error import ParsingError


T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        pass

    def get_lexer(self: T, file: str) -> vbaLexer:
        if Path(file).exists():
            input_stream = FileStream(file)
            return vbaLexer(input_stream)
        raise Exception('file does not exist')

    def lint(self: T, dir: RuleDirectory, code: str) -> list:
        rules = dir.get_loaded_rules()
        lexer = self.get_lexer(code)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())
        e999 = ParsingError()
        ts1 = CommonTokenStream(lexer)
        output = e999.test(ts1)
        program = e999.program
        lexer = self.get_lexer(code)
        ts = CommonTokenStream(lexer)
        token = ts.LT(1)
        if output == []:
            while not token.type == Token.EOF:
                for key in rules:
                    rule = rules[key]
                    output.extend(rule.test(ts))
                ts.consume()
                token = ts.LT(1)
            listener = vbaListener()
            listener.set_token_stream(ts1)
            ParseTreeWalker.DEFAULT.walk(listener, program)

            output.sort()
        return output
