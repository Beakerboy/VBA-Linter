from typing import TypeVar

T = TypeVar('T', bound='RuleBase')


class RuleBase:
    def create_message(self: T, data: tuple) -> str:
        return ':' + str(data[0]) + ':' + str(data[1]) + ' '
