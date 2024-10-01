from . import all_nodes, exit_node

def update_db():
    update_all = all_nodes.all_nodes()
    if update_all == True:
        all = 1
    else:
        all = 0
    update_exit = exit_node.exit_node()
    if update_exit == True:
        exit = 1
    else:
        exit = 0
    
    if all == 1 and exit == 1:
        return True
    else:
        return False
