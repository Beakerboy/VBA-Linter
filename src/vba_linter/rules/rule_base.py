from typing import Type, TypeVar

T = TypeVar('T', bound='RuleBase')


class RuleBase:
    def __init__(self: T) -> None:
        self._rule_name = ""

    def create_message(self: T, data: tuple) -> str:
        return ':' + str(data[0]) + ':' + str(data[1]) + ': ' + self._rule_name + " "

    @classmethod
    def split_nl(cls: Type[T], nl: str) -> list:
        """
        split a newline token into separate line-end characters.
        """
        num = len(nl)
        i = 0
        result = []
        while i < num:
            if num >= 2 and nl[i:i+2] == '\r\n':
                result.append('\r\n')
                i += 2
            else:
                result.append(nl[i:i+1])
                i += 1
        return result
