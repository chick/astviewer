import ast


def square_it(x):
    return x * x


class Transformer1(ast.NodeTransformer):
    pass

