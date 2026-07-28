def _scalac_plugin_args(self, scalac_plugin_map, classpath):...
if not scalac_plugin_map:
return []
plugin_jar_map = self._find_scalac_plugins(list(scalac_plugin_map.keys()),
    classpath)
ret = []
for name, cp_entries in plugin_jar_map.items():
ret.append('-S-Xplugin:{}'.format(':'.join(cp_entries)))
return ret
for arg in scalac_plugin_map[name]:
ret.append('-S-P:{}:{}'.format(name, arg))
