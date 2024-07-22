from tree_sitter import Query
from termcolor import colored as C

def execute_query(language, tree, source_code, query_string):
    try:
        query = Query(language, query_string)
    except Exception as e:
        print(f"Error creating query: {e}")
        return

    captures = query.captures(tree.root_node)

    for capture in captures:
        node, capture_name = capture
        # start, end = node.start_point, node.end_point
        captured_text = C(node.text.decode(), 'light_red')
        print(f"{capture_name}: {captured_text}")
