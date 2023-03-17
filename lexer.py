import math
from tokens import Token, TokenType, ErrorType

SYMBOLS = ["+", "-", "/", "*", "%", "(", ")", "^"]
CONSTS = {"pi": math.pi, "e": math.e}


class Lexer:
    expr = ""
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
            self.parse_const()

    def parse_num(self) -> None:
        if self.i >= len(self.expr):
            return

        is_float = False
        start = self.i

        for _ in self.expr[self.i:]:
            c = self.expr[self.i]
            if c.isnumeric():
                self.i += 1
            elif c == ".":
                if is_float:  # if already a float, there's an extra .
                    self.tokens.append(Token(i=self.i, type=TokenType.ERROR))
                    self.i += 1
                    return
                is_float = True
                self.i += 1
            else:
                break

        end = self.i

        if start == end:
            return

        self.tokens.append(
            Token(i=self.i,
                  type=TokenType.NUM,
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
        while (self.i < len(self.expr) and not self.expr[self.i].isnumeric()
               and self.expr[self.i] not in SYMBOLS):
            self.i += 1

    def parse_const(self) -> None:
        pass

    def check_invalid(self) -> None:
        pass  # TODO