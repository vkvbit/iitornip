import requests

def all_nodes():
    url = 'https://www.dan.me.uk/torlist/?full'
    response = requests.get(url)
    tor_nodes = response.text.split('\n')
    
    with open('db/tor_nodes.txt', 'w') as f:
        for node in tor_nodes:
            f.write(node + '\n')
    
    if response.status_code == 200:
        return True
    else:
        return False  

def check_all_nodes(input_ip):
    with open('db/tor_nodes.txt', 'r') as f:
        tor_nodes = f.read().split('\n')
    
    if input_ip in tor_nodes:
        return True
    else:
        return False