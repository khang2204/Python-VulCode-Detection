def process_module(module):...
if module.name in processed or module.exclude_from_cmake:
return
processed.add(module.name)
for c in sorted(module.children, key=lambda x: x.name):
process_module(c)
dump_options(module)
if module is not root and exists(join(module.directory, 'CMakeLists.txt')):
cmakelists_rows.append('add_subdirectory(%s)\n' % module.directory)
