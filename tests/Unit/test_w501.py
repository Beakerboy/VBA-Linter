import pytest
from antlr4 import InputStream
from antlr.vbaLexer import vbaLexer
from vba_linter.rules.w501 import W501


def test_line_length() -> None:
    code = ('Public Function Supercalifragilisticexpialidocious('
            'atrocious, precocious, indubitably)\r\nEnd Function\r\n')
    input_stream = InputStream(code)
    lexer = vbaLexer(input_stream)
    tokens = lexer.getAllTokens()
    
    assert rule.test(tokens) == [(1, 86, 'W501')]
