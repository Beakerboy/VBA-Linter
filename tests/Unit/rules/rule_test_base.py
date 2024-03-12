import random
import string
from antlr4 import CommonTokenStream, ParseTreeWalker, Token
from antlr4_vba.vbaParser import vbaParser
from pathlib import Path
from typing import Type, TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.listener_rule_base import ListenerRuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    best_practice: list = [
        [
            ('Attribute VB_Name = "SQLFactory"\r\n' +
             'Option Explicit\r\n' +
             'Private Declare PtrSafe Function Foo Lib "bar" (ByVal baz as LongPtr) as LongPtr\r\n' +
             '\r\n' +
             'Public Function Foo(ByRef num As String, _\r\n' +
             'bar)\r\n' +
             '    bar = data(1)\r\n' +
             '    base = (2 + 1)\r\n' +
             '    Dim Foo()    As String\r\n' +
             '    Set Qux = Foo.Bar(2, , base)\r\n' +
             '    x = 3:    y = 4\r\n' +
             '    List.Reverse , 1\r\n' +
             'End Function\r\n'),
            []
        ]
    ]

    function = 'Supercalifragilisticexpialidocious'
    worst_practice = (
        'Attribute VB_Name = "Foo"\r\n' +
        'Public Function ' + function +
        ' ( atrocious ,  precocious, indubitably ) \n' +
        '\n' +
        '\r\n' +
        '\r\n' +
        'I  =  (2+1)\n' +
        '    foo_val=6\r\n'
        '    Let BarVal  =  7\r\n'
        'End Function\n' +
        '\r\n' +
        'Function O()\r\n' +
        'End Function\r\n' +
        '\r\n'
    )

    @classmethod
    def save_code(cls: Type[T], code: str) -> str:
        file_name = RuleTestBase.create_filename(ext='.bas')
        p = Path(file_name)
        with p.open(mode='a') as fi:
            fi.write(code)
        return file_name

    @classmethod
    def delete_code(cls: Type[T], file_name: str) -> None:
        p = Path(file_name)
        p.unlink()

    @classmethod
    def create_tokens(cls: Type[T], file_name: str) -> CommonTokenStream:
        linter = Linter()
        lexer = linter.get_lexer(file_name)
        return CommonTokenStream(lexer)

    @classmethod
    def run_test(cls: Type[T], rule: RuleBase, code: str) -> list:
        file_name = cls.save_code(code)
        ts = cls.create_tokens(file_name)
        results = []
        if isinstance(rule, ListenerRuleBase):
            rule.output = []
            parser = vbaParser(ts)
            program = parser.startRule()
            ParseTreeWalker.DEFAULT.walk(rule, program)
            results.extend(rule.output)
        else:
            results.extend(cls.run_token_rule(rule, ts))
        cls.delete_code(file_name)
        results.sort()
        return results

    @classmethod
    def run_combo_test(cls: Type[T], rule: ListenerRuleBase,
                       code: str) -> list:
        file_name = cls.save_code(code)
        ts = cls.create_tokens(file_name)
        results = []
        rule.output = []
        results.extend(cls.run_token_rule(rule, ts))
        ts.reset()
        parser = vbaParser(ts)
        program = parser.startRule()
        ParseTreeWalker.DEFAULT.walk(rule, program)
        results.extend(rule.output)
        cls.delete_code(file_name)
        results.sort()
        return results

    @classmethod
    def run_token_rule(cls: Type[T],
                       rule: RuleBase,
                       ts: CommonTokenStream) -> list:
        """
        Walk the tokenstream, testing each token against the rule.
        """
        results = []
        while not ts.fetchedEOF:
            results.extend(rule.test(ts))
            token = ts.LT(1)
            assert isinstance(token, Token)
            if token.type != Token.EOF:
                ts.consume()
        return results

    @classmethod
    def create_filename(cls: Type[T], num: int = 16, ext: str = ".txt") -> str:
        chars = random.choice(string.ascii_lowercase)
        file_name = ''.join(chars for i in range(num))
        return file_name + ext
