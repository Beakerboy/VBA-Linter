import pytest
from antlr4 import TerminalNodeImpl, Token
from antlr4_vba.vbaParser import vbaParser
from Unit.rules.rule_test_base import RuleTestBase
from vba_linter.rules.rule_base import RuleBase
from vba_linter.rules.listeners.missing_let import MissingLet


anti_patterns = [
    [
        RuleTestBase.worst_practice,
        [(6, 1, '201'), (7, 5, '201')]
    ]
]


rule = MissingLet()


@pytest.mark.parametrize('rule', [rule])
@pytest.mark.parametrize(
    "code, expected", anti_patterns
)
def test_test(rule: RuleBase, code: str, expected: tuple) -> None:
    assert RuleTestBase.run_test(rule, code) == expected


def test_context() -> None:
    ctx = vbaParser.LetStatementContext()
    ident = Token()
    ident.type = vbaLexer.IDENTIFIER
    ident.text = 'I'
    ident.line = 6
    ident.column = 0
    ident_node = TerminalNodeImpl(ident)
    ambig = vbaParser.AmbiguousIdentifierContext(uname)
    ambig.addChild(ident)
    ident.parentCtx = ambig
    le = vbaParser.LExpressionContext(ctx)
    sn = vbaParser.SimpleNameExpressionContext(le)
    name = vbaParser.NameContext(se)
    uname = vbaParser.UntypedNameContext(name)
    ambig = vbaParser.AmbiguousIdentifierContext(uname)
    eq = Token()
    eq.type = vbaLexer.EQ
    eq.text = '='
    eq.line = 6
    eq.column = 1
    eq_node = TerminalNodeImpl(eq)
    eq_node.parentCtx = ctx
    val = Token()
    val.type = vbaLexer.INTEGERLITERAL
    val.text = '4'
    val.line = 6
    val.column = 2
    val_node = TerminalNodeImpl(val)
    ex = vbaParser.ExpressionContext(ls)
    li = vbaParser.LiteralExpressionContext(ex)
    li.addChild(val_node)
    val_node.parentCtx = li
    ctx.children = [le, eq_node, ex]
    ctx.start = ident
    ctx.stop = val
    rule.enterLetStatement(ctx)
    assert rule.output == [(6, 1, '201')]
