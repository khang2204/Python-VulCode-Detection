def create_directory_tree(path):...
"""docstring"""
path = str(path)
pathlib.Path(path).mkdir(parents=True, exist_ok=True)
