import re

token_specification = [
    ('NUMBER',   r'\d+'),
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
    ('ASSIGN',   r'='),
    ('END',      r';'),
    ('OP',       r'[+\-*/]'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('GT',       r'>'),
    ('SKIP',     r'[ \t\n]+'),
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def lexer(code):
    keywords = {'print', 'if', 'let'}
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'ID' and value in keywords:
            kind = value.upper()
        if kind != 'SKIP':
            yield (kind, value)