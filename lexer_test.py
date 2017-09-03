#!/usr/bin/env python

import unittest
from token import Token
from lexer import Lexer


class ExpectedToken:
    def __init__(self, expected_type, expected_literal):
        self.expected_type = expected_type
        self.expected_literal = expected_literal


class TestLexer(unittest.TestCase):

    def test_next_token(self):
        input = '=+(){},;'
        tests = [
            ExpectedToken(Token.ASSIGN, "="),
            ExpectedToken(Token.PLUS, "+"),
            ExpectedToken(Token.LPAREN, "("),
            ExpectedToken(Token.RPAREN, ")"),
            ExpectedToken(Token.LBRACE, "{"),
            ExpectedToken(Token.RBRACE, "}"),
            ExpectedToken(Token.COMMA, ","),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.EOF, "")
        ]

        lexer = Lexer(input)

        for test in tests:
            token = lexer.next_token()
            self.assertEqual(token.type, test.expected_type)
            self.assertEqual(token.literal, test.expected_literal)

if __name__ == '__main__':
    unittest.main()


