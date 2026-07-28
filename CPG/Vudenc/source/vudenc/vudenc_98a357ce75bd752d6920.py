def dump_yml_filedir(root_dir):...
"""docstring"""
result = load_yml_filedir(root_dir)
json.dump(result, sys.stdout, indent=2)
