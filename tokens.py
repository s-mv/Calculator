from enum import Enum


# enums
class TokenType(Enum):
    NONE = 0
    NUM = 1
    OP = 2
    ERROR = 3


class ErrorType(Enum):
    SYNTAX = 0


# not enums
class Token:
    i = 0
    type = TokenType.NONE
    data = 0

    def __init__(self, i=0, type=TokenType.NONE, data=0) -> None:
        self.i = i
        self.type = type
        self.data = data

    def __repr__(self) -> str:
        return "error" if self.type == TokenType.ERROR else str(self.data)
