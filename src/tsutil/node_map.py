from termcolor import colored

def get_node_types(language):
    return [language.node_type_for_id(i) for i in range(language.node_type_count)]

def print_node(node, source_code, node_types):
    node_type = node_types[node.type_id]
    node_text = source_code[node.start_byte:node.end_byte]
    
    print(f"{node_type}: {colored(node_text, 'green')}")

    for child in node.children:
        print_node(child, source_code, node_types)

def print_node_type_mapping(language):
    for i in range(language.node_type_count):
        node_type = language.node_type_for_id(i)
        is_named = language.node_type_is_named(i)
        is_visible = language.node_type_is_visible(i)
        is_hidden = node_type.startswith('_')
        
        print(f"{i}: kind={colored(node_type, 'green')}, named={is_named}, hidden={is_hidden}, visible={is_visible}")
