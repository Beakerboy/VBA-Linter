from enum import Enum


# class syntax
class Severity(Enum):
    FAILURE = 1
    ERROR = 2
    WARNING = 3
    NOTICE = 4
    DEPRECATION = 5
