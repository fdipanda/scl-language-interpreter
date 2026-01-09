import re
from typing import List
from tokens import Token, TokenType


# Keywords for SCL subset
KEYWORDS = {
    "set", "input", "display",
    "if", "else", "endif",
    "return"
}

# Operators
OPERATORS = {
    "==", "!=", "<=", ">=",
    "<", ">", "=", "+", "-", "*", "/"
}

# Special characters
SPECIALS = {"(", ")"}


class LexicalError(Exception):
    pass


class Scanner:

    @staticmethod
    def from_file(path: str) -> List[Token]:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        return Scanner.scan(src)

    @staticmethod
    def scan(source: str) -> List[Token]:
        # Remove comments (same as your D1 scanner)
        source = re.sub(r"//.*", "", source)
        source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)

        # Regex to match numbers, identifiers, strings, ops, specials
        token_pattern = r'''
            (\d+\.\d+)                |   # real number
            (\d+)                     |   # integer
            ("[^"\n]*")               |   # string literal
            ([a-zA-Z_]\w*)            |   # identifier/keyword
            (==|!=|<=|>=)             |   # two-char operators
            [=+\-*/<>()]                  # specials
        '''

        matches = re.finditer(token_pattern, source, re.VERBOSE)

        tokens = []
        for match in matches:
            lexeme = match.group(0)

            # Keyword
            if lexeme in KEYWORDS:
                tokens.append(Token(TokenType.KEYWORD, lexeme, -1, -1))
            # Operator
            elif lexeme in OPERATORS:
                tokens.append(Token(TokenType.OPERATOR, lexeme, -1, -1))
            # Special
            elif lexeme in SPECIALS:
                tokens.append(Token(TokenType.SPECIAL, lexeme, -1, -1))
            # Real number
            elif re.fullmatch(r"\d+\.\d+", lexeme):
                tokens.append(Token(TokenType.REAL, lexeme, -1, -1))
            # Integer
            elif re.fullmatch(r"\d+", lexeme):
                tokens.append(Token(TokenType.INTEGER, lexeme, -1, -1))
            # String
            elif re.fullmatch(r"\"[^\"\n]*\"", lexeme):
                tokens.append(Token(TokenType.STRING, lexeme, -1, -1))
            # Identifier
            else:
                tokens.append(Token(TokenType.IDENTIFIER, lexeme, -1, -1))

        # Eof token
        tokens.append(Token(TokenType.EOF, "", -1, -1))

        return tokens



if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file.scl>")
        exit(0)
    for t in Scanner.from_file(sys.argv[1]):
        print(t)
