from enum import Enum
import math

# constants
SYMBOLS = ['+', '-', '/', '*', '%', '(', ')', '^', ]
CONSTS = {'pi': math.pi, 'e': math.e}

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


class Lexer:
    expr = ''
    i = 0
    tokens = []

    def __init__(self, expr) -> None:
        self.tokens = []
        self.expr = expr
        self.i = 0

    def lex(self) -> None:
        for _ in self.expr:
            self.check_invalid()
            self.clear_whitespace()
            self.parse_num()
            self.parse_op()

    def parse_num(self) -> None:
        if self.i >= len(self.expr):
            return
        is_float = False
        start = self.i

        for _ in self.expr[self.i:]:
            c = self.expr[self.i]
            if c.isnumeric():
                self.i += 1
            elif c == '.':
                if (is_float):  # if already a float, there's an extra .
                    self.tokens.append(Token(i=self.i, type=TokenType.ERROR))
                    return
                self.i += 1
            else:
                break

        end = self.i

        if start == end:
            return

        self.tokens.append(Token(i=self.i, type=TokenType.NUM,
                                 data=float(self.expr[start:end])))

    def parse_op(self) -> None:
        if self.i >= len(self.expr):
            return
        if self.expr[self.i] in SYMBOLS:
            self.tokens.append(
                Token(i=self.i, type=TokenType.OP, data=self.expr[self.i]))
            self.i += 1

    def clear_whitespace(self) -> None:
        # the longest line of code ever... or something
        while self.i < len(self.expr) and not self.expr[self.i].isnumeric() and self.expr[self.i] not in SYMBOLS:
            self.i += 1

    def check_invalid(self) -> None:
        pass  # TODO


class NumNode:
    token = Token()

    def __init__(self, token=Token()) -> None:
        self.token = token


class OpNode:
    token = Token()
    left_node = None
    right_node = None


class AST:
    def __init__(self) -> None:
        pass


class Parser:
    i = 1
    tokens = []

    def __init__(self, tokens) -> None:
        self.tokens = tokens

    def parse() -> AST:
        return AST()


def eval(expr) -> float or int or ErrorType:
    lexer = Lexer(expr)
    lexer.lex()
    if TokenType.ERROR in lexer.tokens:
        return ErrorType.SYNTAX
    print([x.data for x in lexer.tokens])
