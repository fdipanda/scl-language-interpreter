# parser.py
from tokens import TokenType
from ast_nodes import (
    Program, AssignStmt, InputStmt, DisplayStmt, ReturnStmt,
    IfStmt, BinaryExpr, NumberLiteral, StringLiteral,
    IdentifierExpr, ParenExpr
)


class ParserError(Exception):
    pass


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    # Basic Helpers

    def peek(self):
        return self.tokens[self.i]

    def advance(self):
        tok = self.tokens[self.i]
        self.i += 1
        return tok

    def accept(self, lexeme):
        if self.peek().lexeme == lexeme:
            self.advance()
            return True
        return False

    def expect(self, lexeme):
        if self.peek().lexeme != lexeme:
            raise ParserError(f"Expected '{lexeme}', got '{self.peek().lexeme}'")
        return self.advance()

    # Entry Point

    def parse_program(self):
        statements = []

        while self.peek().type != TokenType.EOF:
            statements.append(self.parse_statement())

        return Program(statements)

    # Statements

    def parse_statement(self):
        lex = self.peek().lexeme

        if lex == "set":
            return self.parse_set()

        elif lex == "input":
            return self.parse_input()

        elif lex == "display":
            return self.parse_display()

        elif lex == "return":
            return self.parse_return()

        elif lex == "if":
            return self.parse_if()

        else:
            raise ParserError(f"Invalid statement start: '{lex}'")

    def parse_set(self):
        self.expect("set")
        ident = self.advance()
        if ident.type != TokenType.IDENTIFIER:
            raise ParserError("Expected identifier after 'set'")
        self.expect("=")
        expr = self.parse_expression()
        return AssignStmt(ident.lexeme, expr)

    def parse_input(self):
        self.expect("input")
        ident = self.advance()
        if ident.type != TokenType.IDENTIFIER:
            raise ParserError("Expected identifier after 'input'")
        return InputStmt(ident.lexeme)

    def parse_display(self):
        self.expect("display")
        expr = self.parse_expression()
        return DisplayStmt(expr)

    def parse_return(self):
        self.expect("return")
        expr = self.parse_expression()
        return ReturnStmt(expr)


    def parse_if(self):
        self.expect("if")
        condition = self.parse_condition()
        self.expect("then")

        # THEN block
        then_block = []
        while self.peek().lexeme not in ("else", "endif"):
            then_block.append(self.parse_statement())

        # Optional ELSE
        else_block = None
        if self.accept("else"):
            else_block = []
            while self.peek().lexeme != "endif":
                else_block.append(self.parse_statement())

        self.expect("endif")
        return IfStmt(condition, then_block, else_block)


    # Conditions

    def parse_condition(self):
        left = self.parse_expression()
        op = self.peek().lexeme

        if op not in ("==", "!=", "<", ">", "<=", ">="):
            raise ParserError("Expected comparison operator")

        operator = self.advance().lexeme
        right = self.parse_expression()
        return BinaryExpr(left, operator, right)

    # Expressions

    def parse_expression(self):
        expr = self.parse_term()

        while self.peek().lexeme in ("+", "-"):
            op = self.advance().lexeme
            right = self.parse_term()
            expr = BinaryExpr(expr, op, right)

        return expr

    def parse_term(self):
        expr = self.parse_factor()

        while self.peek().lexeme in ("*", "/"):
            op = self.advance().lexeme
            right = self.parse_factor()
            expr = BinaryExpr(expr, op, right)

        return expr

    def parse_factor(self):
        tok = self.peek()


        if self.accept("("):
            expr = self.parse_expression()
            self.expect(")")
            return ParenExpr(expr)

        # (int or real)
        if tok.type == TokenType.INTEGER:
            self.advance()
            return NumberLiteral(float(tok.lexeme))

        if tok.type == TokenType.REAL:
            self.advance()
            return NumberLiteral(float(tok.lexeme))

        # string literal
        if tok.type == TokenType.STRING:
            self.advance()
            return StringLiteral(tok.lexeme.strip('"'))

        # identifier
        if tok.type == TokenType.IDENTIFIER:
            self.advance()
            return IdentifierExpr(tok.lexeme)

        raise ParserError(f"Unexpected token in expression: {tok.lexeme}")
