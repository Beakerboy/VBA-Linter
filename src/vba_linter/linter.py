import re
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer
from typing import Type, TypeVar


T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        pass

    def lint(self: T, code: str) -> list:
        max_len = 80
        input_stream = InputStream(code)
        lexer = vbaLexer(input_stream)
        tokens = lexer.getAllTokens()
        line_num = 1
        output: list[tuple] = []
        prev_tok = None
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if token.column > max_len:
                    output.append((token.line, "W501", token.column))
                if not (prev_tok is None) and prev_tok.type == vbaLexer.WS:
                    output.append((token.line, "W200"))
                num = len(token.text)
                i = 0
                while i < num:
                    if num >= 2 and token.text[i:i+2] == '\r\n':
                        i += 2
                    else:
                        output.append((line_num, "W500"))
                        i += 1
                    line_num += 1
            prev_tok = token

        # End of file checks
        final_token = prev_tok
        if final_token is None or final_token.type != vbaLexer.NEWLINE:
            output.append((final_token.line, "W201"))
        elif final_token.type == vbaLexer.NEWLINE:
            newline_list = Linter.split_nl(final_token.text)
            num_nl = len(newline_list)
            if num_nl > 1:
                for i in range(num_nl - 1):
                    output.append((line_num - num_nl + 1 + i, "W300"))
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
    def is_snake_case(cls: Type[T], name: str) -> bool:
        pattern = '[a-z]+(_[a-z]+)*$'
        match = re.match(pattern, name)
        if match:
            return True
        return False

    @classmethod
    def is_camel_case(cls: Type[T], name: str) -> bool:
        """
        Also known as lowerCamelCase.
        """
        pattern = '[a-z]{2,}([a-zA-Z]([a-z])+)*$'
        match = re.match(pattern, name)
        if match:
            return True
        return False
