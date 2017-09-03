#!/usr/bin/env python

from token import Token


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.read_position = 0
        self.char = None

        self.read_char()

    def next_token(self):
        token = {
            Token.ASSIGN: Token(Token.ASSIGN, self.char),
            Token.SEMICOLON: Token(Token.SEMICOLON, self.char),
            Token.LPAREN: Token(Token.LPAREN, self.char),
            Token.RPAREN: Token(Token.RPAREN, self.char),
            Token.COMMA: Token(Token.COMMA, self.char),
            Token.PLUS: Token(Token.PLUS, self.char),
            Token.LBRACE: Token(Token.LBRACE, self.char),
            Token.RBRACE: Token(Token.RBRACE, self.char),
            0: Token(Token.EOF, "")
        }.get(self.char, Token(Token.ILLEGAL, self.char))

        self.read_char()

        return token

    def read_char(self):
        if self.read_position >= len(self.input):
            self.char = 0
        else:
            self.char = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1
