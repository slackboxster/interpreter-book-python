#!/usr/bin/env python

from token import Token
import string

class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.read_position = 0
        self.char = None

        self.read_char()

    def next_token(self):
        self.skip_whitespace()

        tokens = {
            # Operators
            Token.ASSIGN: Token(Token.ASSIGN, self.char),
            Token.PLUS: Token(Token.PLUS, self.char),
            Token.MINUS: Token(Token.MINUS, self.char),
            Token.BANG: Token(Token.BANG, self.char),
            Token.ASTERISK: Token(Token.ASTERISK, self.char),
            Token.SLASH: Token(Token.SLASH, self.char),
            Token.LT: Token(Token.LT, self.char),
            Token.GT: Token(Token.GT, self.char),

            # Delimiters
            Token.COMMA: Token(Token.COMMA, self.char),
            Token.SEMICOLON: Token(Token.SEMICOLON, self.char),
            Token.LPAREN: Token(Token.LPAREN, self.char),
            Token.RPAREN: Token(Token.RPAREN, self.char),
            Token.LBRACE: Token(Token.LBRACE, self.char),
            Token.RBRACE: Token(Token.RBRACE, self.char),

            0: Token(Token.EOF, "")
        }

        if self.char in tokens:
            token = tokens[self.char]
        else:
            if self.is_letter(self.char):
                identifier = self.read_identifier()
                return Token(Token.find_identifier_token_type(identifier), identifier)
            elif self.is_digit(self.char):
                return Token(Token.INT, self.read_number())
            else:
                token = Token(Token.ILLEGAL, self.char)

        self.read_char()

        return token

    def read_char(self):
        if self.read_position >= len(self.input):
            self.char = 0
        else:
            self.char = self.input[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def read_identifier(self):
        position = self.position

        while self.is_letter(self.char):
            self.read_char()

        return self.input[position:self.position]

    def read_number(self):
        position = self.position

        while self.is_digit(self.char):
            self.read_char()

        return self.input[position:self.position]

    def skip_whitespace(self):
        while self.is_whitespace(self.char):
            self.read_char()

    @staticmethod
    def is_letter(byte):
        return str(byte) in (string.ascii_letters + '_')

    @staticmethod
    def is_whitespace(byte):
        return str(byte) in string.whitespace

    @staticmethod
    def is_digit(byte):
        return str(byte) in string.digits


if __name__ == '__main__':
    import sys

    with open(sys.argv[1], 'r') as source_file:
        code = source_file.read()
        lexer = Lexer(code)
        token = lexer.next_token()
        while token.type != Token.EOF:
            print token.type + ": '" + token.literal + "'"
            token = lexer.next_token()
