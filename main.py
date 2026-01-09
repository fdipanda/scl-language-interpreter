from scanner import Scanner
from parser import Parser
from interpreter import Interpreter


def main():
    path = input("Enter .scl filename: ")

    # 1. Load + scan
    tokens = Scanner.from_file(path)

    # 2. Parse into AST
    parser = Parser(tokens)
    program = parser.parse_program()

    # 3. Run the interpreter
    interp = Interpreter()
    interp.run(program)


if __name__ == "__main__":
    main()
