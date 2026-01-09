from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    OPERATOR = auto()
    INTEGER = auto()
    REAL = auto()
    STRING = auto()
    SPECIAL = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int

    def __str__(self) -> str:
        return f"{self.type.name:<9} @({self.line},{self.column}): {self.lexeme}"
