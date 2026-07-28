def load_yml_filedir(root_dir):...
"""docstring"""
if os.path.exists(root_dir):
return _load_yml_filedir(root_dir)[1]
return {}
