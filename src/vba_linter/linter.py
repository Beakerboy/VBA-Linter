from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker, Token
from antlr4_vba.vbaLexer import vbaLexer
from vba_linter.antlr.throwing_error_listener import ThrowingErrorListener
from vba_linter.antlr.vbaListener import VbaListener
from pathlib import Path
from typing import TypeVar
from vba_linter.rule_directory import RuleDirectory
from vba_linter.rules.parsing_error import ParsingError


T = TypeVar('T', bound='Linter')


class Linter:
    # class default constructor
    def __init__(self: T) -> None:
        # Read config file and set parameters for rules
        self.pretty: CommonTokenStream

    def get_lexer(self: T, file: str) -> vbaLexer:
        if Path(file).exists():
            input_stream = FileStream(file, 'utf-8')
            return vbaLexer(input_stream)
        raise Exception('file does not exist')

    def lint(self: T, dir: RuleDirectory, code: str) -> list:
        rules = dir.get_loaded_rules()
        try:
            lexer = self.get_lexer(code)
        except Exception as e:
            return [(0, 0, '999', str(e))]
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())
        e999 = ParsingError()
        ts1 = CommonTokenStream(lexer)
        output = e999.test(ts1)
        lexer = self.get_lexer(code)
        ts = CommonTokenStream(lexer)
        if output == []:
            program = e999.program
            token = ts.LT(1)
            assert token is not None
            while not token.type == Token.EOF:
                # Walk the stream and test the token against
                # each rule.
                for key in rules:
                    rule = rules[key]
                    output.extend(rule.test(ts))
                ts.consume()
                token = ts.LT(1)
                assert token is not None
            listener = VbaListener()
            listener.set_token_stream(ts1)
            listener.listeners = dir.get_parser_rules()
            ParseTreeWalker.DEFAULT.walk(listener, program)
            output.extend(listener.get_output())
            # Get the ignore list and remove violations
            # that should be removed.
            rule_disabler = dir.get_rule_disabler()
            ignored = rule_disabler.ignored
            self.debug = ""
            self.debug += "Ignored Len = " + str(len(ignored)) + "\n"
            if len(ignored) > 0:
                self.debug += "num violations = " + str(len(output)) + "\n"
                for violation in output:
                    violated_rule = violation[2]
                    if violated_rule in ignored:
                        violation_line = violation[0]
                        if violation_line in ignored[violated_rule]:
                            output.remove(violation)
            output.sort()
        self.pretty = ts
        return output

    def get_pretty_code(self: T) -> str:
        code = ""
        size = len(self.pretty.tokens)
        i = 0
        for token in self.pretty.tokens:
            if i + 1 < size:
                code += token.text
            i += 1
        return code
