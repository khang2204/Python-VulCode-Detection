def install_config(config_path, template_root, output_path, validate,...
config = strip_hash(collect_config.collect_config(config_path,
    fallback_metadata), subhash)
tree = build_tree(template_paths(template_root), config)
if not validate:
for path, contents in tree.items():
write_file(os.path.join(output_path, strip_prefix('/', path)), contents)
