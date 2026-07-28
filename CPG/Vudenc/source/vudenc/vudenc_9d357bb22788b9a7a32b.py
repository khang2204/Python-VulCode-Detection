def generate_config_file(self):...
"""docstring"""
config_lines = self.config_file()
config_file = ''
if config_lines is not None:
for i, line in enumerate(config_lines):
return config_file
config_lines[i] = line if line.endswith('\n') else line + '\n'
config_fd, config_file = tempfile.mkstemp()
os.close(config_fd)
conf_file.writelines(config_lines)
