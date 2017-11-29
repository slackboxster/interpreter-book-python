from ast import Program
from lexer import Lexer
from token import Token


class Parser:

    def __init__(self, input):
        self.lexer = Lexer(input)
        self.current_token = self.lexer.next_token()
        self.peek_token = self.lexer.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        return Program()
