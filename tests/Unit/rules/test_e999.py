import pytest
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.linter import Linter
from vba_linter.rules.e999 import E999


anti_patterns = [
    [
        '''\
Public Function Foo(num)
End Sub
''',  # noqa
        [(2, 0, "E999",
          "mismatched input 'End Sub' expecting {'.', '!', 'ACCESS', " +
          "'ADDRESSOF', 'ALIAS', 'AND', 'ATTRIBUTE', 'APPACTIVATE', " +
          "'APPEND', 'AS', 'BEGIN', 'BEEP', 'BINARY', 'BOOLEAN', " +
          "'BYVAL', 'BYREF', 'BYTE', 'CALL', 'CASE', 'CHDIR', " +
          "'CHDRIVE', 'CLASS', 'CLOSE', 'COLLECTION', 'CONST', " +
          "'DATABASE', 'DATE', 'DECLARE', 'DEFBOOL', 'DEFBYTE', " +
          "'DEFDATE', 'DEFDBL', 'DEFDEC', 'DEFCUR', 'DEFINT', " +
          "'DEFLNG', 'DEFOBJ', 'DEFSNG', 'DEFSTR', 'DEFVAR', " +
          "'DELETESETTING', 'DIM', 'DO', 'DOUBLE', 'EACH', 'ELSE', " +
          "'ELSEIF', END_FUNCTION, 'END', 'ENUM', 'EQV', 'ERASE', " +
          "'ERROR', 'EVENT', EXIT_DO, EXIT_FOR, EXIT_FUNCTION, " +
          "EXIT_PROPERTY, EXIT_SUB, 'FALSE', 'FILECOPY', 'FRIEND', " +
          "'FOR', 'FUNCTION', 'GET', 'GLOBAL', 'GOSUB', 'GOTO', 'IF', " +
          "'IMP', 'IMPLEMENTS', 'IN', 'INPUT', 'IS', 'INTEGER', " +
          "'KILL', 'LOAD', 'LOCK', 'LONG', 'LOOP', 'LEN', 'LET', " +
          "'LIB', 'LIKE', LINE_INPUT, 'LSET', '#CONST', '#IF', 'ME', "
          "'MID', 'MKDIR', 'MOD', 'NAME', 'NEXT', 'NEW', 'NOT', " +
          "'NOTHING', 'NULL', 'ON', ON_ERROR, ON_LOCAL_ERROR, 'OPEN', " +
          "'OPTIONAL', 'OR', 'OUTPUT', 'PARAMARRAY', 'PRESERVE', " +
          "'PRINT', 'PRIVATE', 'PUBLIC', 'PUT', 'RANDOM', " +
          "'RANDOMIZE', 'RAISEEVENT', 'READ', 'REDIM', 'REM', " +
          "'RESET', 'RESUME', 'RETURN', 'RMDIR', 'RSET', " +
          "'SAVEPICTURE', 'SAVESETTING', 'SEEK', 'SELECT', " +
          "'SENDKEYS', 'SET', 'SETATTR', 'SHARED', 'SINGLE', 'SPC', " +
          "'STATIC', 'STEP', 'STOP', 'STRING', 'SUB', 'TAB', 'TEXT', " +
          "'THEN', 'TIME', 'TO', 'TRUE', 'TYPE', 'TYPEOF', 'UNLOAD', " +
          "'UNLOCK', 'UNTIL', 'VARIANT', 'VERSION', 'WEND', 'WHILE', " +
          "'WIDTH', 'WITH', 'WITHEVENTS', 'WRITE', 'XOR', " +
          "SHORTLITERAL, INTEGERLITERAL, LINE_CONTINUATION, IDENTIFIER}")]
    ],
    [
        '<?php phpinfo() ?>',
        [(1, 0, "E999", "mismatched input '<?php' expecting <EOF>")]
    ],
]


@pytest.mark.parametrize(
    "code, expected",
    anti_patterns + RuleTestBase.best_practice
)
def test_test(code: str, expected: tuple) -> None:
    rule = E999()
    assert rule.test(Linter().get_lexer(code)) == expected

def test_message() -> None:
    rule = E999()
    data = (1, 0, "E999", "mismatched input '<?php' expecting <EOF>")
    expected = (":1:0: E999 mismatched input '<?php' expecting <EOF>"
    assert rule.create_message(data) == expected
