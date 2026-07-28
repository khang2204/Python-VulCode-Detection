def add_module(parent, name, uri, options, conf, **kwargs):...
if uri is None:
uri = modules[name].urlstring
target_dir = join(subproject_dir, name)
target_dir_rp = os.path.realpath(target_dir)
if not target_dir_rp.startswith(source_dir_rp):
newmodule = Subproject.create(name, uri, target_dir, options, conf, **kwargs)
mod = modules.setdefault(name, newmodule)
if mod is newmodule:
mod.parents.add(parent)
if newmodule.exclude_from_cmake != mod.exclude_from_cmake:
if update:
children_conf = [join(parent.directory, dependency_file) for parent in mod.
    parents]
if not newmodule.same_checkout(mod) and uri is not None:
mod.update()
stack.append(mod)
parent_conf = join(parent.directory, dependency_file)
children = [join(parent.directory, dependency_file) for parent in mod.parents]
for key, value in options.items():
parent.children.add(mod)
parent = join(parent.directory, dependency_file)
mod.options.setdefault(key, value)
if mod.options[key] != value:
