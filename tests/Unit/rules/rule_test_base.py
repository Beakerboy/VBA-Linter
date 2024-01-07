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

    @classmethod
    def tokenize(cls: Type[T], rule: RuleBase, code: str) -> list:
        file_name = RuleTestBase.create_filename(ext='.bas')
        p = Path(file_name)
        with p.open(mode='a') as fi:
            fi.write(code)
        linter = Linter()
        results = []
        lexer = linter.get_lexer(file_name)
        ts = CommonTokenStream(lexer)
        while not ts.fetchedEOF:
            results.extend(rule.test(ts))
            token = ts.LT(1)
            if token.type != Token.EOF:
                ts.consume()
        p.unlink()
        return results

    @classmethod
    def create_filename(cls: Type[T], num: int = 16, ext: str = ".txt") -> str:
        chars = random.choice(string.ascii_lowercase)
        file_name = ''.join(chars for i in range(num))
        return file_name + ext
