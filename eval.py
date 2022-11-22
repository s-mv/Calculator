from enum import Enum


class TokenType(Enum):
    NONE = 0
    NUM = 1
    OP = 2


class ErrorType(Enum):
    SYNTAX = 0


class Token:
    i = 0
    type = TokenType.NONE
    data = 0

def eval(expr) -> float or int or ErrorType:
    # first lex
    for c in expr:
        # check if number
        if c.isnumberic():