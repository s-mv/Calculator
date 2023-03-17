from AST import OpNode, NumNode, AST
from tokens import Token, TokenType, ErrorType


class Parser:
    i = 1
    tokens = []

    def __init__(self, tokens) -> None:
        self.tokens = tokens

    def parse() -> AST:
        return AST()


def eval(expr) -> float or int:
    lexer = Lexer(expr)
    lexer.lex()
    if TokenType.ERROR in lexer.tokens:
        return ErrorType.SYNTAX
    print(lexer.tokens)