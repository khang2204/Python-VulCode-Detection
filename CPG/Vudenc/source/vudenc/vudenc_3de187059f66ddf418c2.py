@staticmethod...
javac_plugin_info_file = os.path.join(resources_dir, _JAVAC_PLUGIN_INFO_FILE)
classname = (javac_plugin_target.classname if PY3 else javac_plugin_target.
    classname.decode('utf-8'))
f.write(classname)
