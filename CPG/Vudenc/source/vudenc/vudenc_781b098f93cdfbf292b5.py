def traverse(path):...
n = dict(name=path, children=[])
for i in os.listdir(path):
if is_folder(path + '/' + i):
return n
n['children'].append(traverse(path + '/' + i))
n['children'].append(dict(name=i))
