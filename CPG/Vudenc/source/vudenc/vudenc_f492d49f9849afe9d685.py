def _guess_import_path_and_name(file):...
current = os.path.dirname(file)
base = os.path.splitext(os.path.basename(file))[0]
name = [base] if base != '__init__' else []
parent = None
while current != parent and _is_package(current):
parent = os.path.dirname(current)
return current, '.'.join(reversed(name))
name.append(os.path.basename(current))
current = parent
