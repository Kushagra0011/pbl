class Node:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

def parse(tokens):
    tokens = list(tokens)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else (None, None)

    def consume(expected_type=None):
        nonlocal pos
        tok = tokens[pos]
        if expected_type and tok[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {tok}")
        pos += 1
        return tok

    def term():
        tok_type, val = peek()
        if tok_type == 'NUMBER':
            consume('NUMBER')
            return Node('number', value=val)
        elif tok_type == 'ID':
            consume('ID')
            return Node('id', value=val)
        else:
            raise SyntaxError(f"Unexpected token in expression: {tok_type}")

    def expression():
        left = term()
        while True:
            tok_type, val = peek()
            if tok_type == 'OP':
                op = consume('OP')
                right = term()
                left = Node('binop', [left, right], value=op[1])
            else:
                break
        return left

    def statement():
        tok_type, val = peek()
        if tok_type == 'LET':
            consume('LET')
            var = consume('ID')
            consume('ASSIGN')
            expr = expression()
            consume('END')
            return Node('assign', [Node('id', value=var[1]), expr])
        elif tok_type == 'PRINT':
            consume('PRINT')
            consume('LPAREN')
            expr = expression()
            consume('RPAREN')
            consume('END')
            return Node('print', [expr])
        else:
            raise SyntaxError(f"Unknown statement starting with {tok_type}")

    stmts = []
    while pos < len(tokens):
        stmts.append(statement())
    return Node('program', stmts)