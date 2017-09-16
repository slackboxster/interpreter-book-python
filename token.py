class Token:

    ILLEGAL="ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENTIFIER = "IDENTIFIER"  # add, foobar, x, y, ...
    INT = "INT"  # 1343456

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"

    keywords = {
        "fn": FUNCTION,
        "let": LET,
        "true": TRUE,
        "false": FALSE,
        "if": IF,
        "else": ELSE,
        "return": RETURN
    }

    def __init__(self, type, literal):
        self.type = type
        self.literal = literal

    @classmethod
    def find_identifier_token_type(cls, identifier):
        if identifier in cls.keywords:
            return cls.keywords[identifier]
        return cls.IDENTIFIER
