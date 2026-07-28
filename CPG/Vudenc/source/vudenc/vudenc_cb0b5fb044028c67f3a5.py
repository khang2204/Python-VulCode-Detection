@staticmethod...
scalac_plugin_info_file = os.path.join(resources_dir, _SCALAC_PLUGIN_INFO_FILE)
f.write(textwrap.dedent(
    """
        <plugin>
          <name>{}</name>
          <classname>{}</classname>
        </plugin>
      """
    .format(scalac_plugin_target.plugin, scalac_plugin_target.classname)).
    strip())
