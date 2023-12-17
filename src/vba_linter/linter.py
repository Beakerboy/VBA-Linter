import re
from antlr4 import InputStream, CommonTokenStream
from antlr.vbaLexer import vbaLexer
from antlr.vbaParser import vbaParser
from typing import Type, TypeVar
from vba_linter.rule_directory import RuleDirectory


T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        pass

    def get_lexer(self: T, code: str) -> vbaLexer:
        input_stream = InputStream(code)
        lexer = vbaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = vbaParser(stream)
        return lexer

    def lint(self: T, code: str) -> list:
        lexer = self.get_lexer(code)
        tokens = lexer.getAllTokens()
        loader = RuleDirectory()
        output = loader.test_all(tokens)
        output.sort()
        return output

    @classmethod
    def text_matches(cls: Type[T], pattern: str, name: str) -> bool:
        match = re.match(pattern, name)
        if match:
            return True
        return False

    @classmethod
    def is_snake_case(cls: Type[T], name: str) -> bool:
        pattern = '(^[a-z]{1}$)|([a-z]+(_[a-z]+)*$)'
        return cls.text_matches(pattern, name)

    @classmethod
    def is_camel_case(cls: Type[T], name: str) -> bool:
        """
        Also known as lowerCamelCase.
        """
        pattern = '(^[a-z]{1}$)|([a-z]{2,}([a-zA-Z]([a-z])+)*$)'
        return cls.text_matches(pattern, name)
