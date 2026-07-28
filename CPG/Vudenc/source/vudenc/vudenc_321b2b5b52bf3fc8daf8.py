def _expected_files_from_dir(dir_index):...
path = MOCK_PATHS[dir_index][0]
files = MOCK_PATHS[dir_index][2]
return [join(path, file) for file in files]
