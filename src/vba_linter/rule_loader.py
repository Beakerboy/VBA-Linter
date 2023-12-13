from typing import TypeVar

T = TypeVar('T', bound='RuleLoader')


class RuleLoader:
    def __init__(self: T) -> None:
        # scan specified rule directory
        # scan ./rules
        # merge list to allow users to override.
        # create list of name to path
        # load config file.
        pass
    
    def test_all(self: T, tokens: list) -> list:
        pass

    def test_rule(self: T, tokens: list) -> list:
        pass
