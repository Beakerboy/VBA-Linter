import random
import string
from antlr4 import CommonTokenStream, Token
from pathlib import Path
from typing import Type, TypeVar
from vba_linter.linter import Linter
from vba_linter.rules.rule_base import RuleBase


T = TypeVar('T', bound='RuleTestBase')


class RuleTestBase:
    best_practice = [
        ['', []],
        ['\r\n', []],
        [
            ('Public Function Foo(num)\r\n' +
             '    bar = data(1)\r\n' +
             '    baz = (2 + 1)\r\n' +
             'End Function\r\n'),
            []
        ]
    ]

    function = 'Supercalifragilisticexpialidocious'
    worst_practice = (
        'Public Function ' + function +
        ' ( atrocious , precocious, indubitably ) \n' +
        '\n' +
        '\r\n' +
        '\r\n' +
        'bar  =  (2+1)\n' +
        'End Function\n' +
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
    def tokenize(cls: Type[T], rule: RuleBase, code: str) -> list:
        file_name = cls.save_code(code)
        ts = cls.create_tokens(file_name)
        results = cls.run_test(rule, ts)
        cls.delete_code(file_name)
        return results

    @classmethod
    def run_test(cls: Type[T], rule: RuleBase, ts: CommonTokenStream) -> list:
        results = []
        while not ts.fetchedEOF:
            results.extend(rule.test(ts))
            token = ts.LT(1)
            if token.type != Token.EOF:
                ts.consume()
        return results

    @classmethod
    def create_filename(cls: Type[T], num: int = 16, ext: str = ".txt") -> str:
        chars = random.choice(string.ascii_lowercase)
        file_name = ''.join(chars for i in range(num))
        return file_name + ext
