def main(argv=sys.argv):...
opts = parse_opts(argv)
if opts.print_templates:
print(opts.templates)
if not opts.metadata:
return 0
if 'OS_CONFIG_FILES' in os.environ:
if opts.templates is None:
logger.error(e)
return 0
opts.metadata = os.environ['OS_CONFIG_FILES'].split(':')
opts.metadata = load_list_from_json(opts.os_config_files)
if opts.key:
return 1
if not opts.metadata and opts.os_config_files == OS_CONFIG_FILES_PATH:
print_key(opts.metadata, opts.key, opts.type, opts.key_default, opts.
    fallback_metadata)
install_config(opts.metadata, opts.templates, opts.output, opts.validate,
    opts.subhash, opts.fallback_metadata)
logger.warning('DEPRECATED: falling back to %s' % OS_CONFIG_FILES_PATH_OLD)
logger.info('success')
opts.metadata = load_list_from_json(OS_CONFIG_FILES_PATH_OLD)
