def append_data_into_file(data, file_path):...
"""docstring"""
contents = yaml.load(file)
contents['entries'].append(data)
yaml.dump(contents, file, default_flow_style=False)
