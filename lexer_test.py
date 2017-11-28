
from tokens import Token
from lexer import Lexer


class ExpectedToken:
    def __init__(self, expected_type, expected_literal):
        self.expected_type = expected_type
        self.expected_literal = expected_literal


class TestLexer:

    def test_next_token_more(self):
        input = '''
            let five = 5;
            let ten = 10;
            let add = fn(x, y) {
                x + y;
            };
            let result = add(five, ten);
            !-/*5
            5 < 10 > 5
            
            if (5 < 10) {
                return true;
            } else {
                return false;
            }
            
            10 == 10;
            10 != 9;
        '''

        tests = [
            ExpectedToken(Token.LET, "let"),
            ExpectedToken(Token.IDENTIFIER, "five"),
            ExpectedToken(Token.ASSIGN, "="),
            ExpectedToken(Token.INT, "5"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.LET, "let"),
            ExpectedToken(Token.IDENTIFIER, "ten"),
            ExpectedToken(Token.ASSIGN, "="),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.LET, "let"),
            ExpectedToken(Token.IDENTIFIER, "add"),
            ExpectedToken(Token.ASSIGN, "="),
            ExpectedToken(Token.FUNCTION, "fn"),
            ExpectedToken(Token.LPAREN, "("),
            ExpectedToken(Token.IDENTIFIER, "x"),
            ExpectedToken(Token.COMMA, ","),
            ExpectedToken(Token.IDENTIFIER, "y"),
            ExpectedToken(Token.RPAREN, ")"),
            ExpectedToken(Token.LBRACE, "{"),
            ExpectedToken(Token.IDENTIFIER, "x"),
            ExpectedToken(Token.PLUS, "+"),
            ExpectedToken(Token.IDENTIFIER, "y"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.RBRACE, "}"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.LET, "let"),
            ExpectedToken(Token.IDENTIFIER, "result"),
            ExpectedToken(Token.ASSIGN, "="),
            ExpectedToken(Token.IDENTIFIER, "add"),
            ExpectedToken(Token.LPAREN, "("),
            ExpectedToken(Token.IDENTIFIER, "five"),
            ExpectedToken(Token.COMMA, ","),
            ExpectedToken(Token.IDENTIFIER, "ten"),
            ExpectedToken(Token.RPAREN, ")"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.BANG, "!"),
            ExpectedToken(Token.MINUS, "-"),
            ExpectedToken(Token.SLASH, "/"),
            ExpectedToken(Token.ASTERISK, "*"),
            ExpectedToken(Token.INT, "5"),
            ExpectedToken(Token.INT, "5"),
            ExpectedToken(Token.LT, "<"),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.GT, ">"),
            ExpectedToken(Token.INT, "5"),
            ExpectedToken(Token.IF, "if"),
            ExpectedToken(Token.LPAREN, "("),
            ExpectedToken(Token.INT, "5"),
            ExpectedToken(Token.LT, "<"),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.RPAREN, ")"),
            ExpectedToken(Token.LBRACE, "{"),
            ExpectedToken(Token.RETURN, "return"),
            ExpectedToken(Token.TRUE, "true"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.RBRACE, "}"),
            ExpectedToken(Token.ELSE, "else"),
            ExpectedToken(Token.LBRACE, "{"),
            ExpectedToken(Token.RETURN, "return"),
            ExpectedToken(Token.FALSE, "false"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.RBRACE, "}"),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.EQ, "=="),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.INT, "10"),
            ExpectedToken(Token.NOT_EQ, "!="),
            ExpectedToken(Token.INT, "9"),
            ExpectedToken(Token.SEMICOLON, ";"),
            ExpectedToken(Token.EOF, "")
        ]

        lexer = Lexer(input)

        for test in tests:
            token = lexer.next_token()
            assert token.type == test.expected_type
            assert token.literal == test.expected_literal

    def test_is_letter(self):
        assert Lexer.is_letter('a')
        assert Lexer.is_letter('Z')
        assert Lexer.is_letter('_')
        assert not Lexer.is_letter('4')
        assert not Lexer.is_letter('$')

    def test_is_whitespace(self):
        assert Lexer.is_whitespace(' ')
        assert Lexer.is_whitespace('\t')
        assert Lexer.is_whitespace('\n')
        assert Lexer.is_whitespace('\r')
        assert not Lexer.is_whitespace('4')
        assert not Lexer.is_whitespace('f')
        assert not Lexer.is_whitespace('$')
        assert not Lexer.is_whitespace('Z')

    def test_is_digit(self):
        assert Lexer.is_digit('9')
        assert not Lexer.is_digit(' ')
        assert not Lexer.is_digit('f')
        assert not Lexer.is_digit('U')
        assert not Lexer.is_digit('$')
        assert not Lexer.is_digit('_')
