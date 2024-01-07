import re
from antlr4 import CommonTokenStream, FileStream
from antlr4_vba.vbaLexer import vbaLexer
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
        e999 = ParsingError()
        output = e999.test(self.get_lexer(code))
        lexer = self.get_lexer(code)
        ts = CommonTokenStream(lexer)
        if output == []:
            for key in rules:
                rule = rules[key]
                output.extend(rule.test(ts))
                ts.consume()
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
