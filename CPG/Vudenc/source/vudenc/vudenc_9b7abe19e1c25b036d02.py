def get_python_files_involved_in_pr(data):...
files = get_files_involved_in_pr(data)
for file in list(files.keys()):
if file[-3:] != '.py':
return files
