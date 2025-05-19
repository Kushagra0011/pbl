def print_ast(node, indent=0):
    print('  ' * indent + node.type + (f": {node.value}" if node.value else ""))
    for child in node.children:
        print_ast(child, indent + 1)