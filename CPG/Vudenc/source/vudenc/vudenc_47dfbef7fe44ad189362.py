@staticmethod...
if tuple(new_file) != tuple(file):
wholediff = Diff.from_string_arrays(file, new_file)
for diff in wholediff.split_diff():
yield diff
