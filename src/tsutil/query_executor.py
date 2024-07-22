from tree_sitter import Query

def execute_query(language, tree, source_code, query_string):
    try:
        query = Query(language, query_string)
    except Exception as e:
        print(f"Error creating query: {e}")
        return

    captures = query.captures(tree.root_node)

    for capture in captures:
        node, capture_name = capture
        start_point, end_point = node.start_point, node.end_point
        captured_text = source_code[node.start_byte:node.end_byte]
        print(f"{capture_name}: {captured_text} ({start_point} - {end_point})")
