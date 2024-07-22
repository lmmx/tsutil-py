from termcolor import colored as C
from textwrap import indent as I

def print_tree(node, source_code, indent=0):
    indent_str = " " * indent
    formatted_node = (
        f"{C(node.type, 'yellow')} "
        f"[grammar_name='{C(node.grammar_name, 'blue')}', "
        f"grammar_id='{C(str(node.grammar_id), 'green')}', "
        f"named='{C(str(node.is_named), 'cyan')}', "
        f"extra='{C(str(node.is_extra), 'magenta')}'] "
        f"{C(str(node.start_point), 'red')} - {C(str(node.end_point), 'red')} "
    )
    text = I(f"{C(str(node.text.decode()), 'light_red')}", prefix=indent_str)

    print(f"{indent_str}{formatted_node}\n{text}")

    for child in node.children:
        print_tree(child, source_code, indent + 2)
