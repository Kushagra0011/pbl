# main.py

from lexer import lexer
from myparser import parse
from ast_printer import print_ast
from interpreter import interpret  # Import the interpreter

if __name__ == '__main__':
    with open("sample_code.txt") as f:
        code = f.read()

    print("\n📦 Tokens:")
    tokens = list(lexer(code))
    for token in tokens:
        print(token)

    print("\n🌲 AST Tree:")
    ast = parse(tokens)
    print_ast(ast)

    print("\n🚀 Interpreter Output:")
    interpret(ast)  # Call the interpreter to run the code
