import requests

def exit_node():
    url = 'https://www.dan.me.uk/torlist/?exit'
    response = requests.get(url)
    exit_nodes = response.text.split('\n')
    
    with open('db/exit_nodes.txt', 'w') as f:
        for node in exit_nodes:
            f.write(node + '\n')
    
    if response.status_code == 200:
        return True
    else:
        return False

def check_exit_node(input_ip):
    with open('db/exit_nodes.txt', 'r') as f:
        exit_nodes = f.read().split('\n')
    
    if input_ip in exit_nodes:
        return True
    else:
        return False
