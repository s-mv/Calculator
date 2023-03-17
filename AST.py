from tokens import Token


class NumNode:
    token = Token()

    def __init__(self, token=Token()) -> None:
        self.token = token


class OpNode:
    token = Token()
    left_node = None
    right_node = None

    def __init__(self, token=Token(), left_node=None, right_node=None) -> None:
        self.token = token
        self.left_node = left_node
        self.right_node = right_node


class AST:

    def __init__(self) -> None:
        pass
