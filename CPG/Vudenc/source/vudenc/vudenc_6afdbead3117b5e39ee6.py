def find_free_port():...
"""docstring"""
port = 8080
max_val = 2 << 16
while test_port(port) and port < max_val:
port += 1
if port == max_val:
return port
