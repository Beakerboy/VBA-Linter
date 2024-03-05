from antlr4 import CommonTokenStream
from antlr4_vba.vbaLexer import vbaLexer as Lexer
from vba_linter.rules.rule_base import RuleBase
from typing import List, TypeVar


T = TypeVar('T', bound='KeywordCaps')


class KeywordCaps(RuleBase):
    """
    report if a keyword is not capitalized
    """
    def __init__(self: T) -> None:
        self._severity = 'E'
        self._rule_name = '220'
        self._message = "Keyword not capitalized"

    def test(self: T, ts: CommonTokenStream) -> list:
        output: List[tuple] = []
        token = ts.LT(1)
        assert token is not None
        # todo: add check for 'VB_Name' type keywords.
        pattern = "^[A-Za-z][A-Za-z]+$"
        text = token.text
        type = token.type
        generics = [
            Lexer.IDENTIFIER, Lexer.ACCESS, Lexer.ALIAS, Lexer.APPACTIVATE,
            Lexer.APPEND, Lexer.BASE, Lexer.BEEP, Lexer.BEGIN, Lexer.BINARY,
            Lexer.CLASS, Lexer.CHDIR, Lexer.CHDRIVE, Lexer.CLASS_INITIALIZE,
            Lexer.CLASS_TERMINATE, Lexer.COLLECTION, Lexer.COMPARE,
            Lexer.DATABASE, Lexer.DELETESETTING, Lexer.ERROR, Lexer.FILECOPY,
            Lexer.GO, Lexer.KILL, Lexer.LOAD, Lexer.LIB, Lexer.LINE,
            Lexer.MID, Lexer.MIDB, Lexer.MID_D, Lexer.MIDB_D, Lexer.MKDIR,
            Lexer.MODULE, Lexer.NAME, Lexer.OBJECT, Lexer.OUTPUT,
            Lexer.PROPERTY, Lexer.RANDOM, Lexer.RANDOMIZE, Lexer.READ,
            Lexer.RESET, Lexer.RMDIR, Lexer.SAVEPICTURE, Lexer.SAVESETTING,
            Lexer.SENDKEYS, Lexer.SETATTR, Lexer.STEP, Lexer.TEXT,
            Lexer.TIME, Lexer.UNLOAD, Lexer.VERSION, Lexer.WIDTH
        ]
        if type not in generics and KeywordCaps.text_matches(pattern, text):
            pattern = "^[A-Z][a-z]+$|ByRef|ByVal|ParamArray|ElseIf|TypeOf|LBound|UBound|ReDim"
            if not KeywordCaps.text_matches(pattern, text):
                line = token.line
                column = token.column
                rule = self._rule_name
                output = [(line, column + 1, rule)]
        return output
