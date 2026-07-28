def clear_holders(base_paths, try_preserve=False):...
"""docstring"""
if not isinstance(base_paths, (list, tuple)):
base_paths = [base_paths]
holder_trees = [gen_holders_tree(path) for path in base_paths]
LOG.info("""Current device storage tree:
%s""", '\n'.join(
    format_holders_tree(tree) for tree in holder_trees))
ordered_devs = plan_shutdown_holder_trees(holder_trees)
for dev_info in ordered_devs:
dev_type = DEV_TYPES.get(dev_info['dev_type'])
shutdown_function = dev_type.get('shutdown')
if not shutdown_function:
if try_preserve and shutdown_function in DATA_DESTROYING_HANDLERS:
LOG.info(
    'shutdown function for holder type: %s is destructive. attempting to preserve data, so not skipping'
     % dev_info['dev_type'])
LOG.info("shutdown running on holder type: '%s' syspath: '%s'", dev_info[
    'dev_type'], dev_info['device'])
shutdown_function(dev_info['device'])
udev.udevadm_settle()
