from ast_nodes import (
    Program, AssignStmt, InputStmt, DisplayStmt, ReturnStmt,
    IfStmt, BinaryExpr, NumberLiteral, StringLiteral,
    IdentifierExpr, ParenExpr
)


class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value


class Interpreter:

    def __init__(self):
        self.memory = {}   # variable storage

    # Main entry

    def run(self, program: Program):
        try:
            for stmt in program.statements:
                self.execute(stmt)
        except ReturnSignal as r:
            # Program stops when return is raised.
            print("Program returned:", r.value)

    # Statement execution

    def execute(self, stmt):
        if isinstance(stmt, AssignStmt):
            value = self.eval_expr(stmt.expression)
            self.memory[stmt.identifier] = value

        elif isinstance(stmt, InputStmt):
            user_input = input(f"Enter value for {stmt.identifier}: ")
            try:
                if "." in user_input:
                    user_input = float(user_input)
                else:
                    user_input = int(user_input)
            except:
                pass
            self.memory[stmt.identifier] = user_input

        elif isinstance(stmt, DisplayStmt):
            value = self.eval_expr(stmt.expression)
            print(value)

        elif isinstance(stmt, ReturnStmt):
            value = self.eval_expr(stmt.expression)
            raise ReturnSignal(value)

        elif isinstance(stmt, IfStmt):
            cond = self.eval_expr(stmt.condition)
            if cond:
                for s in stmt.then_branch:
                    self.execute(s)
            else:
                if stmt.else_branch is not None:
                    for s in stmt.else_branch:
                        self.execute(s)

        else:
            raise Exception(f"Unknown statement type: {type(stmt)}")

    # Expression evaluation

    def eval_expr(self, expr):
        # Number literal
        if isinstance(expr, NumberLiteral):
            return expr.value

        # String literal
        if isinstance(expr, StringLiteral):
            return expr.value

        # Variable reference
        if isinstance(expr, IdentifierExpr):
            if expr.name not in self.memory:
                raise Exception(f"Undefined variable: {expr.name}")
            return self.memory[expr.name]

        # Parenthesized expression
        if isinstance(expr, ParenExpr):
            return self.eval_expr(expr.expr)

        # Binary operators
        if isinstance(expr, BinaryExpr):
            left = self.eval_expr(expr.left)
            right = self.eval_expr(expr.right)
            op = expr.operator

            # Arithmetic
            if op == "+":
                return left + right
            if op == "-":
                return left - right
            if op == "*":
                return left * right
            if op == "/":
                return left / right

            # Comparison / Boolean
            if op == "==":
                return left == right
            if op == "!=":
                return left != right
            if op == "<":
                return left < right
            if op == ">":
                return left > right
            if op == "<=":
                return left <= right
            if op == ">=":
                return left >= right

            raise Exception(f"Unknown operator: {op}")

        raise Exception(f"Unknown expression type: {type(expr)}")
