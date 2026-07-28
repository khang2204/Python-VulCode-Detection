def prepare_socket_file(self, socket_path):...
"""docstring"""
if not os.path.exists(socket_path):
path = os.path.dirname(socket_path)
if not os.path.isdir(path):
try_to_create_directory(path)
