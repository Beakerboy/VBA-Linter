from vba_linter.linter import Linter
from vba_linter.rules.w201 import W201


def test_line_length() -> None:
    code = ('Public Function Foo(num)\r\nEnd Function')
    linter = Linter()
    lexer = linter.get_lexer(code)
    rule = W201()
    assert rule.test(lexer) == [(2, 12, 'W201')]
