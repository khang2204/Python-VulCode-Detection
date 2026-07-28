def check_pythonic_pr(data):...
"""docstring"""
files = list(get_files_involved_in_pr(data).keys())
pythonic = False
for file in files:
if file[-3:] == '.py':
return pythonic
pythonic = True
