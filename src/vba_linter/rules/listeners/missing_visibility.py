def enter_function_sub_stmt(self: T, ctx: ParserRuleContext) -> None:
        child = ctx.getChild(0)
        tok = ctx.start
        if isinstance(child, vbaParser.VisibilityContext):
            if tok.text == "Public":
                self.output.append((tok.line, tok.column + 1,
                                    "Wxxx", "optional public"))
        else:
            line = tok.line
            column = tok.column
            msg = "missing visibility"
            self.output.append((line, column + 1, "Wxxx", msg))
