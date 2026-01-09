# scl-language-interpreter
A Python interpreter for a custom scripting language, implementing lexical analysis, parsing, AST construction, and runtime execution.

## Overview
This project implements a **complete interpreter** for a custom scripting language (`.scl`) using Python.

The interpreter follows a traditional language pipeline:
**lexical analysis → parsing → abstract syntax tree (AST) construction → execution**.

It demonstrates core concepts from **programming languages and compiler theory**, including recursive-descent parsing and AST-based interpretation.

## Language Features
The SCL language supports:
- Variable assignment
- User input
- Display/output statements
- Arithmetic expressions (`+`, `-`, `*`, `/`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Conditional execution (`if / else / endif`)
- Return statements

## Components
- **Scanner (`scanner.py`)**
  - Tokenizes source code
  - Handles keywords, operators, literals, and comments
- **Parser (`parser.py`)**
  - Recursive-descent parser
  - Builds an abstract syntax tree (AST)
- **AST Nodes (`ast_nodes.py`)**
  - Typed node hierarchy using dataclasses
- **Interpreter (`interpreter.py`)**
  - Evaluates the AST
  - Maintains runtime memory
  - Executes statements and expressions
- **Driver (`main.py`)**
  - Coordinates scanning, parsing, and interpretation

## Project Structure
- Core interpreter modules in the root directory
- `examples/` contains sample `.scl` programs used for testing

## How It Works
1. The source file is scanned into tokens
2. Tokens are parsed into an abstract syntax tree
3. The interpreter evaluates the AST
4. Program output is produced during execution

## How to Run
```bash
python main.py
```

When prompted, enter the path to a `.scl` source file.

Example:
```text
Enter .scl filename: examples/welcome.scl
```

## Academic Context
This project was developed to practice:
- Programming language implementation
- Lexical and syntax analysis
- AST construction and traversal
- Interpreter design and execution semantics

## Author
Franck Dipanda
