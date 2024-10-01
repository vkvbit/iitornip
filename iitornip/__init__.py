from . import all_nodes, exit_node
import sys
import os


def iitornip(input_ip, node):
    exit_file = 'db/exit_nodes.txt'
    all_file = 'db/tor_nodes.txt'
    if os.path.exists(all_file) and os.path.exists(exit_file):
        if node == 'all':
            return all_nodes.check_all_nodes(input_ip)
        elif node == 'exit':
            return exit_node.check_exit_node(input_ip)
        else:
            return "Invalid node type. Please use all or exit."
    else:
        print('Database files not found. Please update the database first.')
        sys.exit()
    


