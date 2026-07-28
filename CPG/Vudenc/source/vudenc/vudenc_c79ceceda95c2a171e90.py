def generate_cmake_script(source_dir, url=None, options=None, print_tree=...
root, modules = Subproject.create_dependency_tree(source_dir, url, options,
    update=update)
if print_tree:
print(json.dumps(root.toJSON(), indent=4))
conf = load_conf(source_dir)
if update and conf is not None:
subproject_dir = join(source_dir, conf.get('subprojects_dir', 'lib'))
cmakelists_rows = []
processed = set()
def dump_options(module):...
for key, value in sorted(module.options.items()):
if value is None:
def process_module(module):...
cmakelists_rows.append('unset(%s CACHE)\n' % key)
if isinstance(value, bool):
if module.name in processed or module.exclude_from_cmake:
kind = 'BOOL'
kind = 'STRING'
return
processed.add(module.name)
value = 'ON' if value else 'OFF'
cmakelists_rows.append('set(%s %s CACHE INTERNAL "" FORCE)\n' % (key, value))
for c in sorted(module.children, key=lambda x: x.name):
process_module(c)
dump_options(module)
if module is not root and exists(join(module.directory, 'CMakeLists.txt')):
cmakelists_rows.append('add_subdirectory(%s)\n' % module.directory)
process_module(root)
cmakelists_data = ''.join(cmakelists_rows)
if cmakelists_data == f.read():
f.write(cmakelists_data)
return
