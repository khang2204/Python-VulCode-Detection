def __init__(self, database, options):...
def find_open_port():...
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 0))
port = sock.getsockname()[1]
sock.close()
return port
