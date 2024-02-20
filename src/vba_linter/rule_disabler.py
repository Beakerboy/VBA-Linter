from antlr4.tree.Tree import TerminalNode, TerminalNodeImpl
from antlr4_vba.vbaParser import vbaParser as Parser
from typing import Dict, List, TypeVar
from vba_linter.antlr.vbaListener import VbaListener


T = TypeVar('T', bound='RuleDisabler')


class RuleDisabler(VbaListener):
    def __init__(self: T) -> None:
        super().__init__()
        self.rule_name = "000"
        self.open_blocks: Dict[str, int] = {}
        self.ignored: List[tuple] = []

    def enterClassBeginBlock(  # noqa: N802
            self: T,
            ctx: Parser.ClassBeginBlockContext) -> None:
        ('151', ctx.start.line, ctx.stop.line)

    def enterCommentBody(self: T,  # noqa: N802
                         ctx: Parser.CommentBodyContext) -> None:
        tok = ctx.start
        if tok.text[:9] == "' #noqa: ":
            rule = ctx.start.text[10:13]
            if tok.column == 1:
                # ignore multiple lines
                self.open_blocks[rule] = tok.line
            else:
                # ignore one line
                self.ignored.append((rule, tok.line, tok.line))
        elif tok.text[:9] == "' #qa: ":
            rule = tok.text[8:11]
            if rule in self.open_blocks:
                start_line = self.open_blocks[rule]
                self.ignored.append((rule, start_line, tok.line))

    def visitTerminal(self: T,  # noqa: N802
                      node: TerminalNode) -> None:
        assert isinstance(node, TerminalNodeImpl)
        end_line = node.symbol.line
        for rule in self.open_blocks:
            start_line = self.open_blocks[rule]
            self.ignored.append((rule, start_line, end_line))
