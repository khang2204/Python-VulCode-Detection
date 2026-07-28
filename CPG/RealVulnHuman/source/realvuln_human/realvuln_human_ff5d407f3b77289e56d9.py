basename(f)[:-3]
        for f in all_files
        if isfile(f) and not f.endswith("__init__.py")
    ]

    return trigger_files


def _get_trigger_module(name):
    module_name = "vulnpy.trigger.{}".format(name)
    return import_module(module_name)


def create_trigger_map():
    map = {"home": []}

    trigger_files = _get_trigger_files()

    for vuln_name in trigger_files:
        map.setdefault(vuln_name, [])
