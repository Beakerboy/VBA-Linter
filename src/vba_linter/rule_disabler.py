from antlr4.tree.Tree import TerminalNode, TerminalNodeImpl
from antlr4_vba.vbaParser import vbaParser as Parser
from typing import Dict, TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='RuleDisabler')


class RuleDisabler(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self._rule_name = "000"
        self.open_blocks: Dict[str, int] = {}

        # Key: rule name
        # value: list of line numbers in which the rule is ignored.
        self.ignored: Dict[str, set] = {}

    def enterStartRule(  # noqa: N802
            self: T,
            ctx: Parser.StartRuleContext) -> None:
        self.ignored = {}

    def enterClassBeginBlock(  # noqa: N802
            self: T,
            ctx: Parser.ClassBeginBlockContext) -> None:
        self.add_ignored_lines('151', ctx.start.line, ctx.stop.line)

    def enterCommentBody(self: T,  # noqa: N802
                         ctx: Parser.CommentBodyContext) -> None:
        tok = ctx.start
        if tok.text[:8] == "' #noqa: ":
            rule = ctx.start.text[8:]
            if tok.column == 1:
                # ignore multiple lines
                self.open_blocks[rule] = tok.line
            else:
                # ignore one line
                self.add_ignored_line(rule, tok.line)
        elif tok.text[:7] == "' #qa: ":
            rule = tok.text[7:]
            if rule in self.open_blocks:
                start_line = self.open_blocks[rule]
                self.add_ignored_lines(rule, start_line, tok.line)

    def visitTerminal(self: T,  # noqa: N802
                      node: TerminalNode) -> None:
        assert isinstance(node, TerminalNodeImpl)
        end_line = node.symbol.line
        for rule in self.open_blocks:
            start_line = self.open_blocks[rule]
            self.add_ignored_lines(rule, start_line, end_line)

    def add_ignored_line(self: T, rule: str, line: int) -> None:
        if rule in self.ignored:
            lines = self.ignored[rule]
        else:
            lines = set()
        lines.add(line)
        new = {rule: lines}
        self.ignored.update(new)

    def add_ignored_lines(
            self: T, rule: str, start_line: int, end_line: int
    ) -> None:
        if rule in self.ignored:
            lines = self.ignored[rule]
        else:
            lines = set()
        lines.update(range(start_line, end_line))
        new = {rule: lines}
        self.ignored.update(new)
