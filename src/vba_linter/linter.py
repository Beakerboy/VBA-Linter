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
        input_stream = InputStream(code)
        lexer = vbaLexer(input_stream)
        tokens = lexer.getAllTokens()
        line_num = 1
        output = []
        prev_tok = None
        for token in tokens:
            if token.type == vbaLexer.NEWLINE:
                if not (prev_tok is None) and prev_tok.type == vbaLexer.WS:
                    output.append((line_num, "W200"))
                num = len(token.text)
                i = 0
                while i < num:
                    if num >= 2 and token.text[i:i+2] == '\r\n':
                        line_num += 1
                        i += 2
                    else:
                        output.append((line_num, "W500"))
                        line_num += 1
                        i += 1
            prev_tok = token
        if prev_tok is None or prev_tok.type != vbaLexer.NEWLINE:
            output.append((line_num, "W201"))
        elif prev_tok.type != vbaLexer.NEWLINE:
            
        output.sort()
        return output

    @classmethod
    def split_ws(cls: Type[T], ws: str) -> list:
        """
        split a whitespace token into separate whitespace characters.
        """
        num = len(ws)
        i = 0
        result = []
        while i < num:
            if num >= 2 and ws[i:i+2] == '\r\n':
                result.append('\r\n')
            else:
                result.append(ws[i:i+1])
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
