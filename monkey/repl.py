#!/usr/bin/env python

##
# This is the main file for the monkey interpreter.
##

from lexer import Lexer
from token import Token


def lex(code):
    lexer = Lexer(code)
    token = lexer.next_token()
    while token.type != Token.EOF:
        print token.type + ": '" + token.literal + "'"
        token = lexer.next_token()


if __name__ == '__main__':
    import sys

    REPL_PROMPT = ">> "

    if len(sys.argv) >= 2:
        with open(sys.argv[1], 'r') as source_file:
            code = source_file.read()
            lex(code)

    else:
        code = raw_input(REPL_PROMPT)
        while code != "exit()":
            lex(code)
            code = raw_input(REPL_PROMPT)
