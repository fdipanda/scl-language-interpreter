from dataclasses import dataclass
from typing import List, Optional

class ASTNode:

    pass


class Statement(ASTNode):

    pass

@dataclass
class Program(ASTNode):
    statements: List[Statement]


@dataclass
class AssignStmt(Statement):
    identifier: str
    expression: ASTNode


@dataclass
class InputStmt(Statement):
    identifier: str


@dataclass
class DisplayStmt(Statement):
    expression: ASTNode


@dataclass
class ReturnStmt(Statement):
    expression: ASTNode


@dataclass
class IfStmt(Statement):
    condition: ASTNode
    then_branch: List[Statement]
    else_branch: Optional[List[Statement]]


class Expression(ASTNode):

    pass


@dataclass
class BinaryExpr(Expression):
    left: Expression
    operator: str
    right: Expression


@dataclass
class NumberLiteral(Expression):
    value: float


@dataclass
class StringLiteral(Expression):
    value: str


@dataclass
class IdentifierExpr(Expression):
    name: str    


@dataclass
class ParenExpr(Expression):
    expr: Expression
