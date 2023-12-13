from vba_linter.linter import Linter
from vba_linter.rules.w501 import W501


def test_line_length() -> None:
    code = ('Public Function Supercalifragilisticexpialidocious('
            'atrocious, precocious, indubitably)\r\nEnd Function\r\n')
    linter = Linter()
    lexer = linter.get_lexer(code)
    tokens = lexer.getAllTokens()
    rule = W501()
    assert rule.test(tokens) == [(1, 86, 'W501')]
