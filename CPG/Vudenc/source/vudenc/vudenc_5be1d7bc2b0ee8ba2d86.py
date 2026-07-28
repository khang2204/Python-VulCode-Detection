def build_tree(templates, config):...
res = {}
for in_file, out_file in templates:
res[out_file] = render_template(in_file, config)
return res
