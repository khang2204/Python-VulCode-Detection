@staticmethod...
"""docstring"""
if not os.path.exists(analysis_path):
dirs, files = [], []
for filename in os.listdir(analysis_path):
path = os.path.join(analysis_path, filename)
return dirs, files
if os.path.isdir(path):
dirs.append((filename, len(os.listdir(path))))
files.append(filename)
