@staticmethod...
source_dir_rp = os.path.realpath(source_dir)
root = Subproject.create('root', url, source_dir, {}, {}, toplevel=True)
if url and update:
root.checkout()
conf = load_conf(source_dir)
if conf is None:
return root, {}
subproject_dir = join(source_dir, conf.get('subprojects_dir', 'lib'))
stack = [root]
modules = {}
def get_option(key):...
return root.options[key]
err = e
for module in modules.values():
def add_module(parent, name, uri, options, conf, **kwargs):...
return module.options[key]
err = e
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
freeze_conf = join(root.directory, freeze_file)
if mod.options[key] != value:
if exists(freeze_conf):
freeze_dict = json.load(f)
freeze_dict = {}
if update:
mkdir(subproject_dir)
while len(stack):
current_module = stack.pop()
return root, modules
if current_module.external_project:
generate_cmake_script(current_module.directory, update=update)
conf = load_conf(current_module.directory)
if conf:
if current_module.toplevel:
current_module.options = conf.get('toplevel_options', {})
for name, depobject in conf.get('depends', {}).items():
if options:
external_project = depobject.get('external_project', False)
for key, optobjects in conf.get('optdepends', {}).items():
current_module.options.update(options)
add_module(current_module, name, freeze_dict.get(name, depobject.get('url',
    None)), depobject.get('options', {}), depobject, exclude_from_cmake=
    depobject.get('exclude_from_cmake', external_project), external_project
    =external_project)
if isinstance(optobjects, dict):
optobjects = [optobjects]
for optobject in optobjects:
value = get_option(key)
if value == optobject['value']:
for name, depobject in optobject['depends'].items():
add_module(current_module, name, freeze_dict.get(name, depobject.get('url',
    None)), depobject.get('options', {}), depobject)
