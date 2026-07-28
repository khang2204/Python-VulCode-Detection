def template_paths(root):...
res = []
for cur_root, _subdirs, files in os.walk(root):
for f in files:
return res
inout = os.path.join(cur_root, f), os.path.join(strip_prefix(root, cur_root), f
    )
res.append(inout)
