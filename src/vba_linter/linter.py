import re
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer
from typing import Type, TypeVar
from vba_linter.rule_loader import RuleLoader


T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        pass

    def get_lexer(self: T, code: str) -> vbaLexer:
        input_stream = InputStream(code)
        return vbaLexer(input_stream)

    def lint(self: T, code: str) -> list:
        lexer = self.get_lexer(code)
        tokens = lexer.getAllTokens()
        loader = RuleLoader()
        output = loader.test_all(tokens)

        # End of file checks
        final_token = tokens[-1]
        if not (final_token is None or final_token.type != vbaLexer.NEWLINE):
            newline_list = Linter.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                for i in range(num_nl - 1):
                    output.append((final_token.line + i + 1, "W300"))
        output.sort()
        return output

    @classmethod
    def split_nl(cls: Type[T], nl: str) -> list:
        """
        split a newline token into separate line end characters.
        """
        num = len(nl)
        i = 0
        result = []
        while i < num:
            if num >= 2 and nl[i:i+2] == '\r\n':
                result.append('\r\n')
                i += 2
            else:
                result.append(nl[i:i+1])
                i += 1
        return result

    @classmethod
    def text_matches(cls: Type[T], pattern: str, name: str) -> bool:
        match = re.match(pattern, name)
        if match:
            return True
        return False

    @classmethod
    def is_snake_case(cls: Type[T], name: str) -> bool:
        pattern = '[a-z]|[a-z]+(_[a-z]+)*$'
        return cls.text_matches(pattern, name)

    @classmethod
    def is_camel_case(cls: Type[T], name: str) -> bool:
        """
        Also known as lowerCamelCase.
        """
        pattern = '[a-z]|[a-z]{2,}([a-zA-Z]([a-z])+)*$'
        return cls.text_matches(pattern, name)
