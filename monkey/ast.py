from token import Token


class Node:
    pass
    # tokenLiteral Method


class Statement(Node):
    pass
    # statementNode method


class Expression(Node):
    pass
    # expressionNode method


class Program(Node):

    def __init__(self):
        self.statements = []


class LetStatement(Statement):

    def __init__(self, letToken, identifier, expression):
        self.token = letToken
        self.name = identifier
        self.expression = expression

class Identifier(Expression):
    def __init__(self, token):
        self.token = token
