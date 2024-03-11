from antlr4 import CommonTokenStream
from typing import TypeVar


T = TypeVar('T', bound='CommonTokenStream')


class TokenStreamStub(CommonTokenStream):

    def __init__(self: T) -> None:
        ...
