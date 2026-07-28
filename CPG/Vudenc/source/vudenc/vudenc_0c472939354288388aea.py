def remove_directory_tree(path):...
"""docstring"""
if os.path.exists(path):
shutil.rmtree(path, ignore_errors=True)
